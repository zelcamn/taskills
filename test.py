import serial


ser = serial.Serial('COM4', 9600)

while True:
    print(str(ser.readline()[:-2].decode('UTF-8')))