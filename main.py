from Utilities.py_serial import Serial
from Utilities.adafruit_mqtt import AdafruitMQTT
from Scheduler.scheduler import Scheduler
from Tasks.watering import Watering
from Tasks.add_task_timer import AddTaskTimer
import threading
import time
import json

sche = Scheduler()
timer_task = AddTaskTimer(sche)
adafruit = AdafruitMQTT()

def start_up_system():
	with open("local_db.json", "r", encoding="utf-8") as file:
		global local_db_data
		local_db_data = json.load(file)
		for schedule in local_db_data:
			print(schedule)
			task = Watering(schedule, adafruit)
			timer_task.add_task(task)

start_up_system()

def process_message_from_broker(client, feed_id, payload):
	print("Receive data from", feed_id, payload)
	global local_db_data
	if (feed_id == "schedules"):
		data = json.loads(payload)
		if (data["action"] == "ADD"):
			del data["action"]
			local_db_data.append(data)

			task = Watering(data, adafruit)
			timer_task.add_task(task)

		elif (data["action"] == "DELETE"):
			target_id = data["id"]
			local_db_data = [item for item in local_db_data if item["id"] != target_id]
			print(local_db_data)

		elif (data["action"] == "UPDATE"):
			pass

		with open("local_db.json", 'w', encoding='utf-8') as file:
			json.dump(local_db_data, file, ensure_ascii=False, indent=2)

adafruit.setOnMessage(process_message_from_broker)

def software_timer():
	while True:
		sche.SCH_Update()
		time.sleep(0.1)

threading.Thread(target=timer_task.check_time, args=()).start()
threading.Thread(target=software_timer, args=()).start()

while True:
	sche.SCH_Dispatch_Tasks()
	time.sleep(0.1)
