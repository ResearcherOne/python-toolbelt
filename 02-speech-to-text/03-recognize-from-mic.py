import speech_recognition as speechRecognition

recognizer = speechRecognition.Recognizer()

print speechRecognition.Microphone.list_microphone_names()

mic = speechRecognition.Microphone()
#mic = speechRecognition.Microphone(device_index=2)

with mic as source:
	print "adjust ambient noise start"
	recognizer.adjust_for_ambient_noise(source)

	print "listen start"
	audio = recognizer.listen(source)

	response = {
		"success": True,
		"error": None,
		"transcription": None
	}

	print "recognize start"
	try:
		response["transcription"] = recognizer.recognize_google(audio)
		print "Result Length: "+str(len(response["transcription"]))
		print "Result: "+response["transcription"]
	except speechRecognition.RequestError: # API was unreachable or unresponsive
		response["success"] = False
		response["error"] = "API unavailable"
		print response["error"]
	except speechRecognition.UnknownValueError: # speech was unintelligible
		response["error"] = "Unable to recognize speech"
		print response["error"]