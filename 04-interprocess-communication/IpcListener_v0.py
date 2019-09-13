import threading
from multiprocessing.connection import Listener
 
class IpcListener(threading.Thread):
	def __init__(self, ipcAddress, ipcPort, ipcSecret):
		super(IpcListener, self).__init__()
		self.isDestroyTriggered = False
		self.messageReceivedQueue = []
		self.ipcAddress = ipcAddress
		self.ipcPort = ipcPort
		self.ipcSecret = ipcSecret
		self.conn = None
		self.listener = None

		address = (self.ipcAddress, self.ipcPort)
		self.listener = Listener(address, authkey=self.ipcSecret)

	def destroy(self):
		self.isDestroyTriggered = True

	def isNewMessageAvailable(self):
		newMessageAvailable = len(self.messageReceivedQueue) > 0
		return newMessageAvailable

	def getNextMessage(self):
		if(len(self.messageReceivedQueue) > 0):
			nextMessage = self.messageReceivedQueue.pop(0)
			return nextMessage
		else:
			return ''

	def run(self):
		while not self.isDestroyTriggered:
			if(self.conn is None):
				self.conn = self.listener.accept()
				print 'connection accepted from', self.listener.last_accepted
			else:
				try:
					newMsg = self.conn.recv()
					self.messageReceivedQueue.append(newMsg)
				except EOFError as error:
					self.conn = None
		if (self.conn is not None):
			self.conn.close()
		if (self.listener is not None):
			self.listener.close()
		print "IpcListener destroyed"

'''
listen
send
'''