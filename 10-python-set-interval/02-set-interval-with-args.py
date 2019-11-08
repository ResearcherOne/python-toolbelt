import time
import signal
from JobTimer import JobTimer
from datetime import timedelta

def foo(arg1, arg2):
    print(time.ctime())
    print(arg1)
    print(arg2)

WAIT_TIME_SECONDS = 1

def signal_handler(signum, frame):
    print("Exiting from the program...")
    exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

job = JobTimer(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=foo, arg1="yo", arg2="hey")
job.daemon = True
job.start()


while True:
    time.sleep(1)