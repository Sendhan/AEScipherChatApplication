import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source: 
	r.adjust_for_ambient_noise(source)
	print('ambient noise corrected start speaking')
	audio = r.listen(source)
	print('audio ready')
print(r.recognize_google(audio))
