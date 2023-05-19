import json
import serial
import sys

with open('setup.json') as json_file:
    data = json.load(json_file)


port     = data["port"]
baudrate = data["baudrate"]
stopbit  = data["stopbit"]
test     = data['test']

def read_data():
    readflag = True
    while readflag:
        line = ser.readline().rstrip().decode('utf-8')
        if len(line) >= 7:
            line = line[-7:-1]
            readflag = False
    print(line)        
    with open('wayb.txt','w') as g:
        dataout = json.dump(line,g)  
		
if test:
	print("In test mode")
else:
	open('wayb.txt', 'w').close()
	ser = serial.Serial(port,baudrate,stopbits = stopbit)
	flag = ser.is_open
	if flag:
		read_data()
	else:
		ser.open()
		read_data()
		ser.close()

