import serial
import time

ser = serial.Serial(
   'COM3',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)

def Send(msg):
    ser.write(str.encode(msg))
    
def Read():
    while True:
        d = ser.read()
        d = d.decode('utf-8', 'ignore')
        d = d.strip()
        if d:
            break
    return d
    
