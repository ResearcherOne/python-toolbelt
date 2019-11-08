import time
import signal
from JobTimer import JobTimer
from datetime import timedelta

def foo():
    print (time.ctime())

WAIT_TIME_SECONDS = 1

def signal_handler(signum, frame):
    print("Exiting from the program...")
    exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)
job = JobTimer(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=foo)
job.daemon = True
job.start()


while True:
    time.sleep(1)