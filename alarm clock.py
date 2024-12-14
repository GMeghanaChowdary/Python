import time
import winsound

def alarm_clock():
    alarm_time = input("Enter alarm time (hh:mm): ")
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up! Time's up!")
            winsound.Beep(1000, 2000)
            break
        time.sleep(60)

alarm_clock()
