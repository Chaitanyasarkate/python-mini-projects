import time
import datetime
import os

def alarm_clock(alarm_time):
    print(f"⏰ Alarm set for {alarm_time}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("🔔 Wake up! Time’s up!")
            try:
                # Windows
                os.system("start alarm.mp3")
            except:
                # Linux/Mac
                os.system("afplay alarm.mp3 || mpg123 alarm.mp3")
            break
        time.sleep(30)

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM): ")
    alarm_clock(alarm_time)
