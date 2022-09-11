import serial

ser=serial.Serial("com4",9600)


while True:
    cmd=input("pls = ")
    cmd=cmd+'\r'
    ser.write(cmd.encode())
