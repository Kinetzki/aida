import pyttsx3

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 150)


def say(audio_string):
    engine.say(audio_string)
    engine.runAndWait()
