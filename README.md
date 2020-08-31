# Veda-AI-DocBot

![](https://github.com/ambujalpha/Veda_AI_DocBot/blob/master/images/main.jpg)

# (I) Introduction : 

This is a talking BOT made for medical purposes for older persons. This can talk to person and can remind them about 
their appointments and medicines with time and can fix appointment and can send mails and at the time to emergency too.
It's created on python and pyrebase(firebase) is used as a database. The complete project comprises of a smart watch 
an app and AI Bot, the data is taken from smart watch to smart app and it send to firebase cloud and it processes the 
data and AI Bot responds according to it.

Usually elderly people are lonely and needs medical help time to time, as health is wealth so focusing on our motto we
bring to you a perfect AI bot to help these elderly people. Fuctions and commands are described in later part.

# (II) Functions :

This was inspired by Iron Man Jarvis project which help him with everything, so we named it Veda to help senior citizen.
Firstly we included the basic medical commands like-

1) Fix my appointment(via firebase date and time will be fixed)

2) Emergency (mail and message will be send to emergency contact list person's)
(this prototype includes mail working functionality)

3) Reminder for medicines

Entertainment part-

As elderly people have weak eyes and shivering hands so it's tough for them to operate internet. We have include basic 
commands for their entertainment purpose.

1) Open Youtube, we can also search specific video

2) Send Email to listed contacts

3) Search XYZ

4) XYZ Wikipedia(It will tell few lines from wikipedia to answer anything)

# (III) Microsoft API

commands included to use using microsoft speech api. Here we didn't needed to include NLP for speech recognition and it's conversion.
Live API via microsoft was helpful for this purpose.

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

Link- https://www.cereproc.com/en/node/645


![](https://github.com/ambujalpha/Veda_AI_DocBot/blob/master/images/api.png)

# (IV) Libraries used :

## Speec_recognition :

Library for performing speech recognition, with support for several engines and APIs, online and offline.

![](https://github.com/ambujalpha/Veda_AI_DocBot/blob/master/images/speech.png)

## pyttsx3(python text to speech) :

A Python3 library used for text to speech conversion.

## Wikipedia :

Wikipedia module to integrate wikipedia search.

![](https://github.com/ambujalpha/Veda_AI_DocBot/blob/master/images/wiki.jfif)

## webbrowser :
The webbrowser module provides a high-level interface to allow displaying Web-based documents to users. Under most circumstances, simply calling the open() function from this module will do the right thing.


![](https://github.com/ambujalpha/Veda_AI_DocBot/blob/master/images/browser.png)

## smtplib :

The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

# (V) Pyrebase/Firebase

A simple python wrapper for the Firebase API.

link- https://github.com/thisbejim/Pyrebase


![](https://github.com/ambujalpha/Veda_AI_DocBot/blob/master/images/pyrebase.jpg)

# (VI) Conclusions :

As project can be further be introduced with various functionality and commands to firther make it more user friendly. We can combine it with App and smart watch for day to day health update of not only elderly people but also of any age group person.
We can also introduce machine learning algorithms to analyse data and output results.The complete project comprises of a smart watch an app and AI Bot, the data is taken from smart watch to smart app and it send to firebase cloud and it processes the data and AI Bot responds according to it.
