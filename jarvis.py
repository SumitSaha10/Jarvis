import os
from datetime import datetime
from re import search
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

#Function for speak 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Function for wishing
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning sir")
    elif(hour>=12 and hour<18):
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

    speak("I am jarvis how can i help you")

#Function for taking commands as voice through mircrophone and recognize 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said {query}")

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

    #Function for sending mails
def sendEmail(to, emailInput):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('example@gmail.com', 'password')
    server.sendmail('example@gmail.com', to, emailInput)
    server.close()


if __name__ == "__main__":
    wishMe()
    while(True):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(result)
        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif "open facebook" in query:
            speak("Opening facebook")
            webbrowser.open("facebook.com")
        elif "the time" in query:
            curTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {curTime}")
        elif "open code" in query:
            pathCode = "C:\\Users\\sumit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(pathCode)
        elif "email to receiver name" in query:
            try:
                speak("What should I send")
                emailInput = takeCommand()
                to = "example@gmail.com"
                print(emailInput)
                sendEmail(to,emailInput)
                speak("Email successfully sent")
            except Exception as e:
                print(e)
                speak("Sorry failed to send email")
        
        elif "exit" in query:
            speak("Ok sir")
            exit()

    