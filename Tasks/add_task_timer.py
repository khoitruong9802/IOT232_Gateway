from datetime import datetime
from Scheduler.scheduler import Scheduler
import time

class AddTaskTimer():

	def __init__(self, scheduler):
		self.list_of_task = []
		self.scheduler = scheduler

	def add_task(self, task):
		self.list_of_task.append([task, 1])
	
	def check_time(self):
		while True:
			time.sleep(1)
			for task in self.list_of_task:
				now = datetime.now()
				current_time = now.strftime("%H:%M")

				if (current_time == task[0].startTime and task[1] == 1):
					print("Add task", task[0].scheduleName)
					self.scheduler.SCH_Add_Task(task[0].run, 0, 1000)
					task[1] = 0
