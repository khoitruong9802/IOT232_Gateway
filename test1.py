
import sys
from Adafruit_IO import MQTTClient
import time
import random
import json
from datetime import datetime


class Scheduler:
    def __init__(self):
        self.cycle = None
        self.flow1 = None
        self.flow2 = None
        self.flow3 = None
        self.isActive = None
        self.schedulerName = None
        self.startTime = None
        self.stopTime = None

    def update(self, data):
        self.cycle = data.get('cycle')
        self.flow1 = data.get('flow1')
        self.flow2 = data.get('flow2')
        self.flow3 = data.get('flow3')
        self.isActive = data.get('isActive')
        self.schedulerName = data.get('schedulerName')
        self.startTime = data.get('startTime')
        self.stopTime = data.get('stopTime')
        

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]


scheduler = Scheduler()

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)

def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload + ", feed id: " + feed_id)
    try:
        data = json.loads(payload)
        if isinstance(data, list) and len(data) > 0:
            scheduler.update(data[0])
            print("Scheduler updated with:", scheduler.__dict__)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()


def manageCycle (clent, scheduler):
    # chon vuon de tuoi
    manageMixer(client, scheduler)
    
    
    
def manageMixer (client, scheduler):
        if scheduler.flow1:
            print(f"Starting flow1 for {scheduler.flow1} seconds")
            client.publish("mixer1", "1")
            time.sleep(scheduler.flow1)
            client.publish("mixer1", "0")

counter = 10
while True:
    counter = counter - 1
    if counter <= 0:
        counter = 10
        #todo
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if (current_time == scheduler.startTime):
            print("111")
            for i in range (scheduler.cycle):
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                if (current_time < scheduler.stopTime):
                    manageCycle(client, scheduler)
        else: 
            print("000")
    time.sleep(1)
    pass