/**********************************************************************
* Filename    : Tracking_Sensor.ino
* Product     : Cokoino 4WD Car Chassis Kit
* Description : Print tracking sensor value.
* Auther      : www.cokoino.com
* Modification: 2022/07/05
**********************************************************************/

#define PIN_TRACKING_LEFT  A1
#define PIN_TRACKING_CENTER A2
#define PIN_TRACKING_RIGHT  A3

u8 sensorValue[4];  //define an array 

void setup() {
  Serial.begin(9600); //set baud rate
  pinMode(PIN_TRACKING_LEFT, INPUT); //
  pinMode(PIN_TRACKING_RIGHT, INPUT); //
  pinMode(PIN_TRACKING_CENTER, INPUT); //
}

void loop() {
  sensorValue[0] = digitalRead(PIN_TRACKING_LEFT);
  sensorValue[1] = digitalRead(PIN_TRACKING_CENTER);
  sensorValue[2] = digitalRead(PIN_TRACKING_RIGHT);
  sensorValue[3] = sensorValue[0] << 2 | sensorValue[1] << 1 | sensorValue[2];
  Serial.print("Sensor Value (L / M / R / ALL) : ");
  for (int i = 0; i < 4; i++) {
    Serial.print(sensorValue[i]);
    Serial.print('\t');
  }
  Serial.print('\n');
  delay(500);
}
