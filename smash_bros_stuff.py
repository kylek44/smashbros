import serial
import syslog
import time
import sys

port = '/dev/ttyACM0'
arduino = serial.Serial(port, 115200, timeout=None)

f = open(sys.argv[1], 'w+')

# msg = arduino.read(24)
# print(str(msg) + '\n\n')

while True:
    msg = arduino.read(64)
    msg = msg.decode('utf-8', errors='ignore')
    msgs = msg.split('2')
    if len(msgs) > 1:
        print(msgs[0], end='\n')
        print(msgs[1], end='')
        f.write(msgs[0] + '\n')
        f.write(msgs[1] + '')
    else:
        print(str(msg), end='')
        f.write(str(msg))

f.close()
