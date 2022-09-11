#define numOfValsRec 2
#define digitsPerValRec 3


int valsRec[numOfValsRec];
int stringLength=numOfValsRec*digitsPerValRec+1;
int counter =0;
bool counterStart=false;
String receivedString;
int buttonState;


void setup() {
        Serial.begin(9600);     // mở serial với baudrate 9600
        pinMode(LED_BUILTIN, OUTPUT);
  pinMode(7, INPUT);
        valsRec[0]=90;
valsRec[1]=90;
}

void receiveData(){
  while (Serial.available()){
    char c = Serial.read();
    if (c=='$'){
      counterStart=true;
    }
    if (counterStart){
      if(counter<stringLength){
        receivedString=String(receivedString+c);
      counter++;
      }
      if(counter>=stringLength){
       for (int i=0;i<numOfValsRec;i++){
        int num=(i*digitsPerValRec)+1;
        valsRec[i]=receivedString.substring(num,num+digitsPerValRec).toInt();
       }
       receivedString="";
       counter=0;
       counterStart=false;
      }
    }

  }
}


void loop() {

receiveData();

buttonState = digitalRead(7);
  if (buttonState == HIGH) {
    // turn LED on:
    valsRec[1]=1;
  } else {
    // turn LED off:
    valsRec[1]=0;
  }


Serial.print(valsRec[0]);
Serial.print(",");
Serial.println(valsRec[1]);
delay(1000);
}