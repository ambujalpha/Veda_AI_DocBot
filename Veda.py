import os
import sys
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib
import pyrebase 

config = {
    'apiKey' : 'AIzaSyAUnFXP_ZUX8PwWNmEpf3FppVphdCtDtZA', 
    'authDomain' : 'my-health-31cc7.firebaseapp.com',
    'databaseURL' : "https://my-health-31cc7.firebaseio.com",
    'storageBucket' : "my-health-31cc7.appspot.com" 
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

heart_beat = db.child("message").get()
beats = heart_beat.val()

#using microsoft speech api
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")

    speak("Hey i am Veda, what can i do for you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    print(query)
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('You Mail','Your Password')
    server.sendmail('2017308@iiitdmj.ac.in',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #logic for exceuting tasks based on query
        if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        
        elif 'beat' in query:
            print(beats['heartRate'])
            a = str(beats['heartRate'])
            speak("Sir, your heart beat per minute is " + a)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Sir...")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Sir...")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening Sir...")

        elif 'play music' in query:
            music_dir = 'D:\\gannaPur\\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'recipe' in query:
            query = query.replace("what", "")
            query = query.replace("is", "")
            query = query.replace("the", "")
            webbrowser.open("https://www.youtube.com/results?search_query="+ query)
            speak("Searching for " + query)
        
        elif 'appointment' in query:
            query = query.replace("for","")
            keyword = 'appointment'
            before_keyword, keyword, after_keyword = query.partition(keyword)
            query1 = after_keyword
            keyword2 = 'on'
            before_keyword, keyword, after_keyword = after_keyword.partition(keyword2)
            date = after_keyword
            alpha = after_keyword
            speak("Fixed appiontment" + "on" + alpha)
            db.child("message").child("time").set(alpha)

        elif 'unwell' in query:
            content = "Your pateint Ambuj Jain is unwell in H-402 Hall4 please send someone as soon as possible"
            to = "jainambuj8@gmail.com@gamil.com"
            sendEmail(to,content)
            speak("I have sent an email to your doctor, someone will be here soon")

        elif 'check up' in query:
            b = db.child("message").get()
            c = b.val()
            d = c['time']
            if d==0:
                speak("Your next checkup is not fixed")
            else:
                speak("Your next checkup is on"+d)

        elif 'email to ambuj' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "jainambuj8@gmail.com@gamil.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("sorry for truble at the moment, you can try again")
        
        elif 'quit' in query:
            exit()
        elif 'end' in query:
            exit()
        elif 'stop' in query:
            exit()
        elif 'bye' in query:
            exit()