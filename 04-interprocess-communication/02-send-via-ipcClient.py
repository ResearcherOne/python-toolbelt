from IpcClient import *
import time

ipcClient = IpcClient('localhost', 6000, "secret password")
ipcClient.daemon = True
ipcClient.start()

try:
	while True:
		ipcClient.sendMessage("keyword-detected")
		time.sleep(20)
except KeyboardInterrupt:
	ipcClient.destroy()
	print 'interrupted'