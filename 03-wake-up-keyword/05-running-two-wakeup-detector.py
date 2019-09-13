from WakeupWordDetector_v0 import *

if __name__ == '__main__':
	libPath = None
	modelFilePath = None
	keywordFilePaths = ['input/hey_see_wah.ppn']
	sensitivities = [0.5] #0.0-1.0, default 0.5
	outputPath = None
	inputDeviceIndex = None

	wakeupDetector = WakeupWordDetector(
		library_path=libPath,
		model_file_path=modelFilePath,
		keyword_file_paths=keywordFilePaths,
		sensitivities=sensitivities,
		output_path=outputPath,
		input_device_index=inputDeviceIndex)
	wakeupDetector.start()

	wakeupDetectorTwo = WakeupWordDetector(
		library_path=libPath,
		model_file_path=modelFilePath,
		keyword_file_paths=keywordFilePaths,
		sensitivities=sensitivities,
		output_path=outputPath,
		input_device_index=inputDeviceIndex)
	wakeupDetectorTwo.start()


	try:
		while True:
			if (wakeupDetector.isWakeupWordDetected()):
				print "[1] wake up word detected."
			else:
				pass

			if (wakeupDetectorTwo.isWakeupWordDetected()):
				print "[2] wake up word detected."
			else:
				pass
	except KeyboardInterrupt:
		wakeupDetector.destroy()
		wakeupDetectorTwo.destroy()
		print 'exiting'