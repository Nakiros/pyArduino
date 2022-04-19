#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 2

#define DHTTYPE    DHT22

DHT_Unified dht(DHTPIN, DHTTYPE);

#define POT_1 A0
#define POT_2 A1
int potVal_1=0;
int potVal_2=0;
float DHT22_Temp = 0.00;
float DHT22_Humi = 0.00;

char pyRequest;

void setup() {
  Serial.begin(115200);
  pinMode(POT_1, INPUT);
  pinMode(POT_2, INPUT);
  dht.begin();
  sensor_t sensor;
  dht.temperature().getSensor(&sensor);
  dht.humidity().getSensor(&sensor);
}

void loop() {
  potVal_1=analogRead(POT_1);
  
  potVal_2=analogRead(POT_2);
  
  sensors_event_t event;
  
  dht.temperature().getEvent(&event);
  if (isnan(event.temperature)) {
    DHT22_Temp=99.9;
  }
  else {
    DHT22_Temp=event.temperature;
  }

  dht.humidity().getEvent(&event);
  if (isnan(event.relative_humidity)) {
    DHT22_Humi=-1.00;
  }
  else {
    DHT22_Humi=event.relative_humidity;
  }
  float mapedVoltage=fmap(potVal_2,0,1023,0.00,5.00);
  
  if (Serial.available()>0){
    pyRequest = Serial.read();
    if (pyRequest == 'g'){
      Serial.print(potVal_1);
      Serial.print(",");
      Serial.print(mapedVoltage,3);
      Serial.print(",");
      Serial.print(DHT22_Temp);
      Serial.print(",");
      Serial.println(DHT22_Humi);
    } // If pyRequest 'g'
  } // Serial.available
} // Void loop

float fmap(float x, float in_min, float in_max, float out_min, float out_max) { return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min; }
