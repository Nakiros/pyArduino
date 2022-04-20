String myCmd;

void setup(){
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
}
void loop(){

while(Serial.available()==0){
  }
myCmd=Serial.readStringUntil('\r');

if (myCmd == "ON"){
  digitalWrite(LED_BUILTIN, HIGH);
  }
if (myCmd == "OFF"){
  digitalWrite(LED_BUILTIN, LOW);
  }
}
