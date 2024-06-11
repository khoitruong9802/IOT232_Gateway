from Adafruit_IO import MQTTClient
from dotenv import load_dotenv
import sys
import os

class AdafruitMQTT:

    def __init__(self):

        if load_dotenv():
            self.AIO_FEED_IDS = ["nutnhan1", "nutnhan2"]
            self.AIO_USERNAME = os.getenv("AIO_USERNAME")
            self.AIO_KEY = os.getenv("AIO_KEY")
        else:
            print("Fail to read from env")
            sys.exit(1)

        self.client = MQTTClient(self.AIO_USERNAME , self.AIO_KEY)
        self.client.on_connect = self._connected
        self.client.on_disconnect = self._disconnected
        self.setOnMessage(self._defaultOnMessage)
        self.client.on_subscribe = self._subscribe
        self.client.connect()
        self.client.loop_background()
        # self.client.loop_blocking()

    def _connected(self, client):
        print("Ket noi thanh cong ...")
        for topic in self.AIO_FEED_IDS:
            self.client.subscribe(topic)

    def _subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribe thanh cong ...")

    def _disconnected(self, client):
        print("Ngat ket noi ...")
        sys.exit(1)

    def _defaultOnMessage(self, client, feed_id, payload):
        print("Nhan du lieu: " + payload + ", feed id: " + feed_id)

    def publish(self, feed_id, value, group_id = None, feed_user = None):
        self.client.publish(feed_id, value, group_id, feed_user)

    def setOnMessage(self, callback):
        self.client.on_message = callback
