# some_file.py
import sys
import numpy as np
# sys.path.insert(0, '/Users/Codeo/yolo_test_MQTT/darkflow/ClearBlade-Python-SDK')
sys.path.insert(0, '/Users/Codeo/yolo_test_MQTT/darkflow/clearblade')
from clearblade.ClearBladeCore import System, Query, Developer, Users
from darkflow.net.build import TFNet
import cv2
import PIL
import scipy
import _pickle as cpickle
from struct import *



import time


url = "http://localhost:3000"

# mySystem = System(SystemKey, SystemSecret, url, safe=False)

SystemKey = "d4a68fb60becb78bcdb4ecdffd2c"
SystemSecret = "D4A68FB60BD2DF8998A5EBC0E5EA01"

mySystem = System(SystemKey, SystemSecret, safe = False)

# Auth as anon
# anon = mySystem.AnonUser()

# Use the anon user to register Martin
# martin = mySystem.registerUser("vsoni@clearblade.com", "ashokverma")

# mySystem.
sanket = mySystem.User("try@email.com", "password")
print("\n HI\n")
# Use Sanket to access a messaging client
mqtt = mySystem.Messaging(sanket)
# result
# options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2-tiny.weights", "threshold": 0.1}
# tfnet = TFNet(options)
imgcv = cv2.imread("./sample_img/sample_dog.jpg")
# result = tfnet.return_predict(imgcv)

# Set up callback functions
def on_connect(client, userdata, flags, rc):
    # When we connect to the broker, subscribe to the southernplayalisticadillacmuzik channel
    client.subscribe("config")
    client.subscribe("predict")
    client.subscribe("predict/results")


def on_message(client, userdata, message):
    # When we receive a message, print it out
    if(message.topic == "config"):{
     print("hi config")
    }
    if(message.topic == "predict"):
        options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2-tiny.weights", "threshold": 0.1}
        tfnet = TFNet(options)

        print(message.payload)
        print(type(message.payload))

        # z=cpickle.loads()
        yo =(message.payload).decode('utf-8')
        g=bytes.fromhex(yo)
        z = cpickle.loads(g)

        result = tfnet.return_predict(z)
        mqtt.publish("predict/results",str(result),0)
        print(result)



# Connect callbacks to client
mqtt.on_connect = on_connect
mqtt.on_message = on_message


# print(result)
# Connect and wait for messages
mqtt.connect()
while (True):
    time.sleep(1000)  # wait for messages

# subscribe to /config

# when message arrives on /config
# build options from message payload
# instantiate TFNet
# wait

# subscribe to /predict
# when message arrives on /predict
# get imge from payload
# run tfnet predict

# publish on /predict/results model results

