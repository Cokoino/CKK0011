# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep

NSLEEP1 = 12
AN11 = 17
AN12 = 27
BN11 = 22
BN12 = 23
NSLEEP2 = 13
AN21 = 24
AN22 = 25
BN21 = 26
BN22 = 16
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(NSLEEP1,GPIO.OUT)
GPIO.setup(NSLEEP2,GPIO.OUT)
GPIO.setup(AN11,GPIO.OUT)
GPIO.setup(AN12,GPIO.OUT)
GPIO.setup(BN11,GPIO.OUT)
GPIO.setup(BN12,GPIO.OUT)
GPIO.setup(AN21,GPIO.OUT)
GPIO.setup(AN22,GPIO.OUT)
GPIO.setup(BN21,GPIO.OUT)
GPIO.setup(BN22,GPIO.OUT)
GPIO.output(AN11,GPIO.LOW)
GPIO.output(AN12,GPIO.LOW)
GPIO.output(BN11,GPIO.LOW)
GPIO.output(BN12,GPIO.LOW)
GPIO.output(AN21,GPIO.LOW)
GPIO.output(AN22,GPIO.LOW)
GPIO.output(BN21,GPIO.LOW)
GPIO.output(BN22,GPIO.LOW)
p1=GPIO.PWM(NSLEEP1,1000)
p2=GPIO.PWM(NSLEEP2,1000)
p1.start(25)
p2.start(25)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high lr-leftrotation rr-rightrotation e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(AN11,GPIO.HIGH)
         GPIO.output(AN12,GPIO.LOW)
         GPIO.output(BN11,GPIO.HIGH)
         GPIO.output(BN12,GPIO.LOW)
         GPIO.output(AN21,GPIO.HIGH)
         GPIO.output(AN22,GPIO.LOW)
         GPIO.output(BN21,GPIO.HIGH)
         GPIO.output(BN22,GPIO.LOW)
         print("backward")
         x='z'
        else:
         GPIO.output(AN11,GPIO.LOW)
         GPIO.output(AN12,GPIO.HIGH)
         GPIO.output(BN11,GPIO.LOW)
         GPIO.output(BN12,GPIO.HIGH)
         GPIO.output(AN21,GPIO.LOW)
         GPIO.output(AN22,GPIO.HIGH)
         GPIO.output(BN21,GPIO.LOW)
         GPIO.output(BN22,GPIO.HIGH)
         print("forward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(AN11,GPIO.LOW)
        GPIO.output(AN12,GPIO.LOW)
        GPIO.output(BN11,GPIO.LOW)
        GPIO.output(BN12,GPIO.LOW)
        GPIO.output(AN21,GPIO.LOW)
        GPIO.output(AN22,GPIO.LOW)
        GPIO.output(BN21,GPIO.LOW)
        GPIO.output(BN22,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(AN11,GPIO.LOW)
        GPIO.output(AN12,GPIO.HIGH)
        GPIO.output(BN11,GPIO.LOW)
        GPIO.output(BN12,GPIO.HIGH)
        GPIO.output(AN21,GPIO.LOW)
        GPIO.output(AN22,GPIO.HIGH)
        GPIO.output(BN21,GPIO.LOW)
        GPIO.output(BN22,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(AN11,GPIO.HIGH)
        GPIO.output(AN12,GPIO.LOW)
        GPIO.output(BN11,GPIO.HIGH)
        GPIO.output(BN12,GPIO.LOW)
        GPIO.output(AN21,GPIO.HIGH)
        GPIO.output(AN22,GPIO.LOW)
        GPIO.output(BN21,GPIO.HIGH)
        GPIO.output(BN22,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='lr':
        print("leftrotation")
        GPIO.output(AN11,GPIO.HIGH)
        GPIO.output(AN12,GPIO.LOW)
        GPIO.output(BN11,GPIO.LOW)
        GPIO.output(BN12,GPIO.HIGH)
        GPIO.output(AN21,GPIO.HIGH)
        GPIO.output(AN22,GPIO.LOW)
        GPIO.output(BN21,GPIO.LOW)
        GPIO.output(BN22,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='rr':
        print("rightrotation")
        GPIO.output(AN11,GPIO.LOW)
        GPIO.output(AN12,GPIO.HIGH)
        GPIO.output(BN11,GPIO.HIGH)
        GPIO.output(BN12,GPIO.LOW)
        GPIO.output(AN21,GPIO.LOW)
        GPIO.output(AN22,GPIO.HIGH)
        GPIO.output(BN21,GPIO.HIGH)
        GPIO.output(BN22,GPIO.LOW)
        temp1=0
        x='z'
        
    elif x=='l':
        print("low")
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        x='z'
    elif x=='m':
        print("medium")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        x='z'
    elif x=='h':
        print("high")
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        x='z'
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

