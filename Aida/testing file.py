import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 500

with sr.Microphone() as voice:
    while True:
        audio = r.listen(voice)
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            pass
