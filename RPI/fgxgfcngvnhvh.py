import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from google.oauth2 import service_account
from google.cloud import firestore
import RPi.GPIO as GPIO
import time, sys
from gpiozero import Servo
from time import sleep

IN_FLOW_SENSOR = 23
OUT_FLOW_SENSOR = 24
TRIG1 = 17   #level in storage
ECHO1 = 27   #level in storage
TRIG2 = 22   #level in canal
ECHO2 = 25   #level in canal
TRIG3 = 0    #level in dam2
ECHO3 = 1    #level in dam2
servo1 = Servo(6)     #rainfall for dam1
servo2 = Servo(5)     #rainfall for dam2
in1 = 10
in2 = 9
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN_FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(OUT_FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(r"/home/pi/Downloads/credential.json", scope)
client = gspread.authorize(creds)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/home/pi/Downloads/MECCLOUDTEST-468f2ea6f2c4.json"
sheet = client.open("MEC ").sheet1


global count1
global count_a
count1 = 0
global count2
count2=0
count_a=count1
global distance_11,distance_1,distance_22,distance2,distance_3,distance_33
distance_11 = 0
distance_1=0
distance_2=0
distance_22=0
distance_33=0
distance_3=0
distance_11 = distance_1
def countPulse1(channel):
   global count1,count_a
   count1 = count1+1
   if count_a==count1-5:
        print("greater than 5")
        count_a=count1
   print("count1 = ",count1,"count_a = ",count_a)

def countPulse2(channel):
   global count2,count_b
   count_b = count2
   count2 = count2+1
   print("count2 = ",count2)

GPIO.add_event_detect(IN_FLOW_SENSOR, GPIO.BOTH, callback=countPulse1)
GPIO.add_event_detect(OUT_FLOW_SENSOR, GPIO.BOTH, callback=countPulse2)

def upload_to_firestore_inflow(inflow):
    db = firestore.Client()
    doc_ref = db.collection(u'users').document(u'B2hzw68AZfJ0Hv0h4ORa')
    doc_ref.update({
        u'inflow': inflow,
        })

def upload_to_firestore_outflow(outflow):
    db = firestore.Client()
    doc_ref = db.collection(u'users').document(u'B2hzw68AZfJ0Hv0h4ORa')
    doc_ref.update({
        u'outflow':outflow,
        })

def upload_to_firestore_level(level):
    db = firestore.Client()
    doc_ref = db.collection(u'users').document(u'B2hzw68AZfJ0Hv0h4ORa')
    doc_ref.update({
        u'level':level,
        })

def upload_to_firestore_level_in_canal(level_in_canal):
    db = firestore.Client()
    doc_ref = db.collection(u'users').document(u'B2hzw68AZfJ0Hv0h4ORa')
    doc_ref.update({
        u'level_in_canal':level_in_canal,
        })

def upload_to_firestore_trigger(trigger):
    db = firestore.Client()
    doc_ref = db.collection(u'users').document(u'B2hzw68AZfJ0Hv0h4ORa')
    doc_ref.update({
        u'trigger':trigger,
        })

def upload_to_firestore_trigger2(trigger):
    db = firestore.Client()
    doc_ref = db.collection(u'users').document(u'B2hzw68AZfJ0Hv0h4ORa')
    doc_ref.update({
        u'trigger2':trigger,
        })

def level1():                      #level in storage
    global distance_11,distance_1
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
    upload_to_firestore_level(distance_1)
    if distance_11 >= distance_1+1 or distance_11 <= distance_1-1:  #check if 1 precision is enough
        print("upload to firestore",distance_1)     #upload data to firestore

def level2():                        #level in canal
    global distance_22,distance_2
    distance_22 = distance_2
    GPIO.output(TRIG2, False)
    time.sleep(2)
    GPIO.output(TRIG2, True)
    time.sleep(0.00001)
    GPIO.output(TRIG2, False)
    while GPIO.input(ECHO2)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO2)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance_2 = pulse_duration*17150
    distance_2 = round(distance_2, 2)
    print("Distance:",distance_2,"cm")
    upload_to_firestore_level(distance_2)
    if distance_22 >= distance_2+1 or distance_22 <= distance_2-1:  #check if 1 precision is enough
        print("upload to firestore",distance_2)     #upload data to firestore

def level3():                       #level in dam2
    global distance_33,distance_3
    distance_33 = distance_3
    GPIO.output(TRIG3, False)
    time.sleep(2)
    GPIO.output(TRIG3, True)
    time.sleep(0.00001)
    GPIO.output(TRIG3, False)
    while GPIO.input(ECHO3)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO3)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance_3 = pulse_duration*17150
    distance_3 = round(distance_3, 2)
    print("Distance:",distance_3,"cm")
    upload_to_firestore_level(distance_3)
    if distance_33 >= distance_3+1 or distance_33 <=distance_3-1:  #check if 1 precision is enough
        print("upload to firestore",distance_3)     #upload data to firestore

def rainfall_motor1_500ml():
    servo1.min()
    sleep(4)          #change the value according to the experiment
    servo1.max()
    sleep(4)          #change the value according  to the experiment

def rainfall_motor1_1l():
    servo1.min()
    sleep(4)          #change the value according to the experiment
    servo1.max()
    sleep(4)          #change the value according to the experiment

def rainfall_motor2_500ml():
    servo2.min()
    sleep(5)        #change the value according to the experiment
    servo2.max()
    sleep(5)
#change the value according to the experiment
while(1):
    level3()
    sleep(2)
    level2()
    sleep(2)