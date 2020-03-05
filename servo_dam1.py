import RPi.GPIO as GPIO
import time, sys
from gpiozero import Servo
from time import sleep

servo1 = Servo(5)
#servo1 = Servo(6)
GPIO.setmode(GPIO.BCM)

servo1.min()
sleep(5)        #change the value according to the experiment
servo1.max()
#sleep(2)        #change the value according to the experiment

