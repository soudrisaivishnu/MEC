import RPi.GPIO as GPIO
import time, sys

TRIG1 = 17   #level in storage
ECHO1 = 27   #level in storage

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)

global distance_11,distance_1
while True:
    GPIO.output(TRIG1, False)
    time.sleep(2)
    GPIO.output(TRIG1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG1, False)
    while GPIO.input(ECHO1)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO1)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance_1 = pulse_duration*17150
    distance_1 = round(distance_1, 2)
    print("Distance:",distance_1,"cm")
    #if distance_11 >= distance_1+1 or distance_11 <= distance_1-1:  #check if 1 precision is enough
    #print("upload to firestore",distance_1)     #upload data to firestore
