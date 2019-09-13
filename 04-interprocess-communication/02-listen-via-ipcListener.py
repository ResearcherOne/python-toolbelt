from IpcListener import *

ipcListener = IpcListener('localhost', 6000, "secret password")
ipcListener.daemon = True
ipcListener.start()

try:
	while True:
		if (ipcListener.isNewMessageAvailable()):
			newMessage = ipcListener.getNextMessage()
			print "message received: "+str(newMessage)
		else:
			pass
except KeyboardInterrupt:
	print 'interrupted'