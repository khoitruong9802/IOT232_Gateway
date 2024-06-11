class Task:
    def __init__(self, _pTask, _Delay, _Period):
        self.pTask = _pTask
        self.Delay = _Delay
        self.Period = _Period

    pTask = None
    Delay = 0
    Period = 0
    RunMe = 0
    TaskID = -1

class Task2:
    def __init__(self):
        print("Init task 2")
        return

    def Task2_Run(self):
        print("Task 2 is activated!!!!")