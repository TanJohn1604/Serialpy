import  serial
import time

def initConnection(port,baud):
    try:
        ser=serial.Serial(port,baud)
        print("Device connected")
        return ser
    except:
        print("Errorrrrrrr")
def sendData(se,data,digits):
    myString="$"
    for d in data:
        myString+= str(d).zfill(digits)
    try:
        se.write(myString.encode())
        print(myString)
    except:
        print("send fail")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ser=initConnection("COM4",9600)
    while True:
        sendData(ser,[1,255],3)
        time.sleep(5)
        sendData(ser, [200, 2], 3)
        time.sleep(5)


