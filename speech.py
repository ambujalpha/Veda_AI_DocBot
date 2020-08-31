import os
import sys
import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print ('say something!')
    audio = r.listen(source)
    
    text = r.recognize_google(audio)
    print('you said: {}'.format(text))

    try:
        print("google thinks you said" +r.recognize_google(audio))

    except:
        print("could not recognize  ")