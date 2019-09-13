import threading
from multiprocessing.connection import Client
 
class IpcClient(threading.Thread):
	def __init__(self, ipcAddress, ipcPort, ipcSecret):
		super(IpcClient, self).__init__()
		self.isDestroyTriggered = False
		self.ipcAddress = ipcAddress
		self.ipcPort = ipcPort
		self.ipcSecret = ipcSecret
		self.conn = None

		address = (self.ipcAddress, self.ipcPort)
		self.conn = Client(address, authkey=self.ipcSecret)

	def destroy(self):
		self.isDestroyTriggered = True

	def sendMessage(self, text):
		self.conn.send(text)

	def run(self):
		while not self.isDestroyTriggered:
			pass
		if (self.conn is not None):
			self.conn.close()
		print "IpcClient destroyed"

'''
listen
send
'''