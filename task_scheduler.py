import time
from datetime import datetime
def task_scheduler():
    while True:
        if datetime.now().minute == 0:
            print("Task executed!")
        time.sleep(60)
task_scheduler()
