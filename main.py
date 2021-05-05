import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

from speech_recognition import Microphone

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12 :
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("i am jarvis sir. plaese tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognizr_google(audio, language = 'en-in')
        print("user said: {query} \n")

    except Expectation as e:
        #print (e)
        print ("say that again please.....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('mail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        #if 1:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak('searching wikipedia.....')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print (results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'open instagram' in query:
                webbrowser.open("instagram.com")

            elif 'play music' in query:
                webbrowser.open("spotify.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak("sir, the time is {strTime}")

            elif 'open code' in query:
                webbrowser.open("udaychugh.github.io")

            elif 'email to harry' in query:
                try:
                    speak("what should i say?")
                    content = takeCommand()
                    to = "youremail@gmail.com"
                    sendEmail(to, content)
                    speak("email has been sent sir")
                except exception as e:
                    print (e)
                    speak("sorry sir, i am not able to send this mail")
