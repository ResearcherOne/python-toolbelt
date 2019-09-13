import threading
import time

class Listener(threading.Thread):
    def __init__(self, listenerName):
        super(Listener, self).__init__()
        self.isDestroyTriggered = False
        self.listenerName = listenerName

    def destroy(self):
        self.isDestroyTriggered = True

    def run(self):
        while not self.isDestroyTriggered:
            time.sleep(1)
            print(self.listenerName+": I am listening.")

        print ("Listener destroyed")

listener = Listener("Bryan")
listener.daemon = True
listener.start()

time.sleep(10)

listener.destroy()