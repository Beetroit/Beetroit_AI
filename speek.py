import pyttsx3
#Module for speech
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()