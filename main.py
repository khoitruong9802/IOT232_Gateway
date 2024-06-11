from Utilities.py_serial import Serial
from Utilities.adafruit_mqtt import AdafruitMQTT
import threading

class Main:
    def __init__(self):
        self.my_ada = AdafruitMQTT()

    def run(self):
        while True:
            pass
        # threading.Thread(target=self.ser.run, args=(self.publishSensor,)).start()
        
if __name__ == "__main__":
    Main().run()