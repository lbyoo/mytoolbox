
import os
import sys
import paho.mqtt.client as mqtt
import time
import random
import user

config = user.config()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.publish("my/topic","hello%f"% time.time())

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.username_pw_set(config["user"],config["password"])
    client.connect(config["mqtt-server"], config["port"], 60)


    client.loop_start()

    with open("input.txt","r", encoding="utf-8") as f:
        txt = f.read()
        infot = client.publish(config["topic"], txt, qos=2)
        infot.wait_for_publish()   
        print(infot)


if __name__ == "__main__":
    main()    







