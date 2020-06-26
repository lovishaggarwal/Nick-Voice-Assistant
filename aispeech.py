import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

"""speak audio function"""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

"""wish function according to time"""
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morrning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am Nick. How may I help you?")
    speak("I am Nick. How may I help you?")

"""It takes microphone input from the user,recoognizes it and returns string output"""
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Say or type anything")
        # query = input("type here:")
        print("Listening...")
        speak("listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("recognising")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Sorry I am unable to understand. Please say it again...")
        speak("Sorry I am unable to understand. Please say it again")
        return "None"
    return query

"""send email function"""
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pycharm.python123@gmail.com', 'python@123')
    server.sendmail('pycharm.python123@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")

        elif 'open gne website' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("www.gndec.ac.in")

        elif 'open google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")

        elif 'open w3schools' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("w3schools.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            randomsongs = random.choice(songs)
            os.startfile(os.path.join(music_dir, randomsongs))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")


        elif 'the weather' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.com/search?q=weather")

        elif 'open notepad' in query:
            os.system('notepad')

        elif 'open calculator' in query:
            os.system('start Calculator:')

        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open gallery' in query:
            codePath = "D:\\Pins"
            os.startfile(codePath)

        elif 'hello nick' in query:
            print("hello sir, how may I help you?")
            speak("hello sir, how may I help you?")

        elif query.startswith('google'):
            speak('Searching google...')
            query1 = query.replace("google ", "")
            query2 = query1.replace(" ","+")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(f"https://www.google.com/search?q={query2}")

        elif query.startswith('translate'):
            query1 = query.replace(" ","+")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(f"https://www.google.com/search?q={query1}")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'alovish0709@gmail.com'
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif 'exit' in query:
            print("Thank you Sir, have a nice day :)")
            speak("Thank You Sir, have a nice day")
            exit()

        else:
            speak('Searching google...')
            query2 = query.replace(" ", "+")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(f"https://www.google.com/search?q={query2}")