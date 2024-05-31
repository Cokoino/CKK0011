/**********************************************************************
* Filename    : Line_Tracking_Car.ino
* Product     : Cokoino 4WD Car Chassis Kit
* Description : Line Tracking Car.
* Auther      : www.cokoino.com
* Modification: 2022/07/05
**********************************************************************/
#include <AFMotor.h>
 AF_DCMotor motor1(1);//define motor1
 AF_DCMotor motor2(2);//define motor2
 AF_DCMotor motor3(3);//define motor3
 AF_DCMotor motor4(4);//define motor4
#define PIN_TRACKING_LEFT A1
#define PIN_TRACKING_CENTER A2
#define PIN_TRACKING_RIGHT  A3

void setup() {
  pinsSetup(); //set up pins
  getTrackingSensorVal();//Calculate Voltage speed Compensation
}

void loop() {
  u8 trackingSensorVal = 0;
  trackingSensorVal = getTrackingSensorVal(); //get sensor value

  switch (trackingSensorVal)
  {
    case 0:   //000//car run stop
      motor1.run(RELEASE);// motor1 stop run
      motor2.run(RELEASE);
      motor3.run(RELEASE);
      motor4.run(RELEASE);
      break;
    case 7:   //111/car move forward
      motor1.setSpeed(200);//setup the speed of motor1
      motor2.setSpeed(200);//setup the speed of motor2
      motor3.setSpeed(200);//setup the speed of motor3
      motor4.setSpeed(200);//setup the speed of motor4
      motor1.run(FORWARD);// motor1 run FORWARD
      motor2.run(FORWARD);
      motor3.run(FORWARD);
      motor4.run(FORWARD);
      break;
    case 1:   //001//car turn
      motor1.setSpeed(150);//setup the speed of motor2
      motor4.setSpeed(150);//setup the speed of motor3
      motor1.run(FORWARD);//motor1 run forward
      motor4.run(FORWARD);
      break;
    case 3:   //011//car turn right
      motor1.setSpeed(100);//setup the speed of motor2
      motor4.setSpeed(100);//setup the speed of motor3
      motor1.run(FORWARD);//motor1 run forward
      motor4.run(FORWARD);
      break;
    case 2:   //010
    case 5:   //101//car move forward
      motor1.setSpeed(200);//setup the speed of motor1
      motor2.setSpeed(200);//setup the speed of motor2
      motor3.setSpeed(200);//setup the speed of motor3
      motor4.setSpeed(200);//setup the speed of motor4
      motor1.run(FORWARD);// motor1 run FORWARD
      motor2.run(FORWARD);
      motor3.run(FORWARD);
      motor4.run(FORWARD);
      break;
    case 6:   //110//car turn left
       motor1.run(RELEASE);// motor1 stop run
       motor4.run(RELEASE);
       motor2.setSpeed(150);//setup the speed of motor2
       motor3.setSpeed(150);//setup the speed of motor3
       motor2.run(FORWARD);// motor2 run FORWARD
       motor3.run(FORWARD);
      break;
    case 4:   //100 //car turn right
       motor1.run(RELEASE);
       motor4.run(RELEASE);
       motor2.setSpeed(150);//setup the speed of motor2
       motor3.setSpeed(150);//setup the speed of motor3
       motor2.run(FORWARD);// motor2 run FORWARD
       motor3.run(FORWARD);
      break;
    default:
      break;
  }
}


//when black line on one side is detected, the value of the side will be 0, or the value is 1
u8 getTrackingSensorVal() {
  u8 trackingSensorVal = 0;
  trackingSensorVal = (digitalRead(PIN_TRACKING_LEFT) == 1 ? 1 : 0) << 2 | (digitalRead(PIN_TRACKING_CENTER) == 1 ? 1 : 0) << 1 | (digitalRead(PIN_TRACKING_RIGHT) == 1 ? 1 : 0) << 0;
  return trackingSensorVal;
}

void pinsSetup() {
  //define tracking sensor pin
  pinMode(PIN_TRACKING_LEFT, INPUT);
  pinMode(PIN_TRACKING_RIGHT, INPUT);
  pinMode(PIN_TRACKING_CENTER, INPUT);
}
