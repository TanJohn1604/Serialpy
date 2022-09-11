import serial
import time
spilitdata=[0,0]
flag=1
def initConnection(port,baud):
    try:
        ser=serial.Serial(port,baud)
        print("Device connected")
        return ser
    except:
        print("Errorrrrrrr")
def sendData(se,data,digits):
    global flag
    myString="$"
    for d in data:
        myString+= str(d).zfill(digits)
    try:
        se.write(myString.encode())
        flag=1
        print(myString)
    except:
        print("send fail")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ser=initConnection("COM4",9600)
    while True:
        if flag==0:
            sendData(ser,[spilitdata[0],spilitdata[1]],3)
        if flag==1:
            while (ser.inWaiting() != 0):
                data = ser.readline()
                data = str(data, 'utf-8')
                data = data.strip('\r\n')
                spilitdata = data.split(",")
                flag=0

        # try:
        # except:
        #     print("read fail")
        spilitdata[0] = int(spilitdata[0]) + 1
        if(spilitdata[0]>990):
            spilitdata[0]=0
        print(spilitdata[0], spilitdata[1])
        time.sleep(1)



