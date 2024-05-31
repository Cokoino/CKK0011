# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep

in1 = 23
in2 = 24
in3 = 25
in4 = 18
in5 = 4
in6 = 17
in7 = 27
in8 = 22
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)
GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)


print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high lr-leftrotation e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         GPIO.output(in5,GPIO.HIGH)
         GPIO.output(in6,GPIO.LOW)
         GPIO.output(in7,GPIO.HIGH)
         GPIO.output(in8,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         GPIO.output(in5,GPIO.LOW)
         GPIO.output(in6,GPIO.HIGH)
         GPIO.output(in7,GPIO.LOW)
         GPIO.output(in8,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.HIGH)
        GPIO.output(in8,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.HIGH)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.HIGH)
        temp1=0
        x='z'
        
    elif x=='lr':
        print("leftrotation")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.HIGH)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.HIGH)
        temp1=0
        x='z'
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

