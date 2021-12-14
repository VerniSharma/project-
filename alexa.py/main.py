import datetime

import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour<=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am alexa , how may i help you verni")



if __name__ == '__main__':
    wishme()

