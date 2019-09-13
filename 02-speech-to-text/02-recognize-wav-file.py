import speech_recognition as sr

print sr.__version__

r = sr.Recognizer()

harvard = sr.AudioFile('input/harvard.wav')
with harvard as source:
	audio = r.record(source)
	result = r.recognize_google(audio)
	print result