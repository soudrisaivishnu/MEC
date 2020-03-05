import RPi.GPIO as GPIO
import time, sys
from gpiozero import Servo
from time import sleep

servo2 = Servo(6)
#servo1 = Servo(6)
GPIO.setmode(GPIO.BCM)

servo2.min()
sleep(5)       #change the value according to the experiment
servo2.max()#change the value according to the experiment
#sleep(5)