from gpiozero import AngularServo
from time import sleep

servo = AngularServo(5,min_angle=0,max_angle=90)
servo.angle=0

servo.min()
sleep(1)
servo.mid()
sleep(1)
servo.max()
sleep(1)