import RPi.GPIO as GPIO
import time, sys
from time import sleep

in1 = 5
in2 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.output(in1,False)
GPIO.output(in2,False)

#GPIO.output(in1,True)
GPIO.output(in2,False)
sleep(10)        #time to open       #give x according to the release value, i.e 1lt or 2lts
#GPIO.output(in1,False)
GPIO.output(in2,True)
#sleep(20)       #time to close       #we do not keep any holding time

