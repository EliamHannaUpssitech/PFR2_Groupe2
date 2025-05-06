import serial
import time

ser = serial.Serial()
ser.port = '/dev/ttyACM0'
ser.baudrate = 115200

ser.open()
print(ser.isOpen())
try:
    time.sleep(2)
    while True:
        line = ser.readline().decode().strip()
        try:
            print(line)
        except:
            print('--')
        
except KeyboardInterrupt:
    ser.close()
