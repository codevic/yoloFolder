# some_file.py
import sys
import numpy as np
# sys.path.insert(0, '/Users/Codeo/yolo_test_MQTT/darkflow/ClearBlade-Python-SDK')
sys.path.insert(0, '/Users/Codeo/yolo_test_MQTT/darkflow/clearblade')
from clearblade.ClearBladeCore import System, Query, Developer, Users
from darkflow.net.build import TFNet
import cv2
import _pickle as cpickle
import base64
import PIL
import scipy

import time

imgcv = cv2.imread("./sample_img/sample_dog.jpg")
print(imgcv.shape)
# a=imgcv.tostring()
# print(type(a))
from numpy import array

# a = np.array([0, 3, 5])
# a_str = ','.join(str(x) for x in imgcv) # '0,3,5'
# a2 = np.array([int(x) for x in a_str.split(',')])
s= (cpickle.dumps(imgcv)).hex()
# np.set_printoptions(threshold=np.nan)
# a = imgcv
# a_str = a.__repr__() # 'array([[0, 3, 5],\n       [2, 3, 4]])'
# Img = eval(a_str) # array([[0, 3, 5],
# imgarr =np.array2string(imgcv)
# z = base64.b64encode(bytes(imgcv))

g=bytes.fromhex(s)

z = cpickle.loads(g)

options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2-tiny.weights", "threshold": 0.1}
tfnet = TFNet(options)
# print(len(message.payload))
# y = base64.b64decode(z)


# Img = np.fromstring(a,dtype='uint8').reshape((576, 768, 3))
# print(Img.shape)
global result; result = tfnet.return_predict(z)
print(result)








# url = "http://localhost:3000"

#
# SystemKey = "d4a68fb60becb78bcdb4ecdffd2c"
# SystemSecret = "D4A68FB60BD2DF8998A5EBC0E5EA01"
#
# mySystem = System(SystemKey, SystemSecret, safe = False)

# mySystem.

# sanket = mySystem.User("try@email.com", "password")
# print("\n HI\n")

# Use Sanket to access a messaging client
# mqtt = mySystem.Messaging(sanket)


# result = tfnet.return_predict(imgcv)

# Set up callback functions
def on_connect(client, userdata, flags, rc):
    # When we connect to the broker, subscribe to the southernplayalisticadillacmuzik channel
    client.subscribe("config")
    client.subscribe("predict")




def on_message(client, userdata, message):
    # When we receive a message, print it out
    if(message.topic == "config"):{
     print("hi config")
    }
    if(message.topic == "predict"):
        options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2-tiny.weights", "threshold": 0.1}
        tfnet = TFNet(options)
        print(len(message.payload))
        Img = np.fromstring(message.payload,dtype='uint8').reshape(107,2,3)
        # print(Img.shape)

        # Img = np.asarray(message.payload, dtype='uint8')
        # global result
        global result; result = tfnet.return_predict(Img)
        print(result)

    # print("Received message "+ str(message.payload) + "on topic " + message.topic )
    # print ("Received message '" + message.payload + "' on topic '" + message.topic + "'")


# # Connect callbacks to client
# mqtt.on_connect = on_connect
# mqtt.on_message = on_message
#
# options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2-tiny.weights", "threshold": 0.1}
# tfnet = TFNet(options)
# # print(len(message.payload))
# Img = np.fromstring(message.payload,dtype='uint8').reshape(107,2,3)
# # print(Img.shape)
#
# # Img = np.asarray(message.payload, dtype='uint8')
# # global result
# global result; result = tfnet.return_predict(Img)
# print(result)


# print(result)
# # Connect and wait for messages
# mqtt.connect()
# while (True):
#     time.sleep(1000)  # wait for messages

