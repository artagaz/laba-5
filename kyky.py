import schedule
import time
from datetime import datetime

def ku():
    hour = datetime.now().hour % 12
    if hour == 00:
        hour = 12
    print("Ку " * hour)

schedule.every().hour.at(":00").do(ku)

while True:
    schedule.run_pending()
    time.sleep(1)