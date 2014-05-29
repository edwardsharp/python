import schedule
import time

def job():
    print("JOBBBB")
    print time.time()

schedule.every().hour.at(':05').do(job)
schedule.every().hour.at(':10').do(job)
schedule.every().hour.at(':15').do(job)
schedule.every().hour.at(':20').do(job)
schedule.every().hour.at(':25').do(job)
schedule.every().hour.at(':30').do(job)
schedule.every().hour.at(':35').do(job)
schedule.every().hour.at(':40').do(job)
schedule.every().hour.at(':45').do(job)
schedule.every().hour.at(':50').do(job)
schedule.every().hour.at(':50').do(job)
schedule.every().hour.at(':00').do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)
