import time

class Watering:
  def __init__(self, data, adafruit):
    self.adafruit = adafruit
    self.cycle = data.get('cycle')
    self.flow1 = data.get('flow1')
    self.flow2 = data.get('flow2')
    self.flow3 = data.get('flow3')
    self.isActive = data.get('isActive')
    self.area = data.get('area')
    self.scheduleName = data.get('scheduleName')
    self.startTime = data.get('startTime')
    self.stopTime = data.get('stopTime')
    self.cycleLeft = data.get('cycle')

  def run(self):
    if (self.cycleLeft > 0):
      print(self.scheduleName, ": Cycle", self.cycle - self.cycleLeft + 1)

      print(self.scheduleName, ": Mixer 1 (Relay 1 ON)")
      self.adafruit.publish("relay1", 1)

      time.sleep(self.flow1 / 2)

      print(self.scheduleName, ": Mixer 1 (Relay 1 OFF)\n")
      self.adafruit.publish("relay1", 0)

      print(self.scheduleName, ": Mixer 2 (Relay 2 ON)")
      self.adafruit.publish("relay2", 1)

      time.sleep(self.flow2 / 2)

      print(self.scheduleName, ": Mixer 2 (Relay 2 OFF)\n")
      self.adafruit.publish("relay2", 0)

      print(self.scheduleName, ": Mixer 3 (Relay 3 ON)")
      self.adafruit.publish("relay3", 1)

      time.sleep(self.flow3 / 2)

      print(self.scheduleName, ": Mixer 3 (Relay 3 OFF)\n")
      self.adafruit.publish("relay3", 0)

      print(self.scheduleName, ": Pump in (Relay 7 ON)")
      self.adafruit.publish("relay7", 1)

      time.sleep(10)

      print(self.scheduleName, ": Pump in (Relay 7 OFF)\n")
      self.adafruit.publish("relay7", 0)

      print(self.scheduleName, ": Select area (Relay", self.area + 3,"ON)\n")
      self.adafruit.publish("relay" + str(self.area + 3), 1)

      print(self.scheduleName, ": Pump out (Relay 8 ON)")
      self.adafruit.publish("relay8", 1)

      time.sleep(10)

      print(self.scheduleName, ": Pump out (Relay 8 OFF)\n")
      self.adafruit.publish("relay8", 0)
      
      self.cycleLeft = self.cycleLeft - 1
    else:
      print(self.scheduleName, "finish!!\n")