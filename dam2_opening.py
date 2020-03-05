import RPi.GPIO as GPIO
import time, sys
from time import sleep

in1 = 10
in2 = 9
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.output(in1,False)
GPIO.output(in2,True)
sleep(8)        #time to open       #give x according to the release value, i.e 1lt or 2lts
GPIO.output(in1,True)
GPIO.output(in2,False)
sleep(8)
print("in in2")#time to close       #we do not keep any holding time
GPIO.output(in1,True)
GPIO.output(in2,True)
sleep(5)
GPIO.output(in1,True)
GPIO.output(in2,True)
