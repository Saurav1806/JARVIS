import ctypes
from urllib import request
from wsgiref import headers

import pyautogui
import pyttsx3
import pywikihow

import requests
import speech_recognition as sr
import datetime
import os
import webbrowser

import wolframalpha
from bs4 import BeautifulSoup
from pyjokes import pyjokes
from twilio.rest.bulkexports.v1.export import day

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio: object) -> object:
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to Convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listesning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:

        speak('say that again please sir')
        return "None"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning Sir")
        speak("I am your assistant")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon sir")
        speak("I am your assistant")
    else:
        speak("Good Evening sir")
        speak("I am your assistant")
    speak("Jarvis 2 point o sir, Please tell me how can i help you?")


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # logic building for task

        if "open ms word" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016"
            os.startfile(npath)


        elif "open notepad" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Notepad"
            os.startfile(npath)

        elif "who is my favourite teacher" in query:
            speak("Sir , as you told me D B M S is your favourite Subject")
            speak("so i think , its Vaishali Maam.")
            takecommand()
            speak("I know sir , she is excellent teacher as well as great mentor also")
            takecommand()
            speak("I would like to meet her someday sir")
            takecommand()
            speak("Thank You sir")

        elif "what is your name" in query:
            speak("My friends call me , jarvis 2 point o Sir")

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, because I have no feelings like humans Sir")

        elif "hello" in query:
            speak("hello sir")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif "also fine" in query or "good" in query:
            speak("It's good to know that your fine")

        elif "i love you" in query:
            speak("I love u too Sir")

        elif "some chat" in query or "some talk" in query:
            speak("on what topic you want to have chat sir")
            takecommand()
            speak("sure sir , i would love to discuss on that")
            takecommand()
            speak("ok sir As you want")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "bye bye" in query or "stop listening" in query:
            speak("Ok sir i am going to quit.")
            speak("Thanks for giving me your time")
            speak("Have a Good day sir")
            exit()



        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "this world" in query:
            speak("Thanks to Saurav. further It's a secret")


        elif "who are you" in query:
            speak("I am your virtual assistant created by Saurav")

        elif "reason for you" in query:
            speak("I was created as a Minor project by Mister Saurav ")

        elif "are you there" in query:
            speak("Yes sir i am here , sorry for interupt Sir , how can i help you sir")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takecommand()
            speak("Great Sir , i like the name Sir ,Thanks for naming me")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            strTime = datetime.datetime.now().strftime("%m/%d/%Y")
            speak(f"Sir, the today is {strTime}")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

        elif "do you play cricket" in query:
            speak("sorry sir , i don't know how to play cricket.")
            speak("could you please teach me that")
            takecommand()
            speak("Thank you sir , i am fast learner")
            speak("i will learn it quickly")

        elif "thank you" in query:
            speak("no need of thank you sir, i am always ready to help you")

        elif "open youtube" in query:
            speak("ok sir")
            speak("what do you want to search")
            query = takecommand()
            web1 = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web1)
            speak("here is your result.")

        elif "close youtube" in query:
            os.system(f"TASKKILL /f /im chrome.exe")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("done sir")

        elif "close google" in query:
            os.system(f"TASKKILL /f /im chrome.exe")

        elif "search on wikipedia" in query:
            speak("what do you want to search sir")
            query = takecommand()
            web3 = "https://en.wikipedia.org//wiki/" + query
            webbrowser.open(web3)

        elif "close wikipedia" in query:
            os.system(f"TASKKILL /f /im chrome.exe")

        elif "open website" in query:
            speak("which website you want to visit")
            query = takecommand()
            web2 = 'http://www.' + query + '.com'
            webbrowser.open(web2)
            speak("here is your result sir")

        elif "close website" in query:
            os.system(f"TASKKILL /f /im chrome.exe")


        elif "music" in query or "song" in query:
            speak("which song do you want to listen")
            query = takecommand()
            if "baby" in query:
                speak("here is your song , enjoy sir")
                os.startfile("C:\\Users\\SANU\\Downloads\\music\\baby.mp3")
            elif "Broken Angel" in query:
                speak("here is your song , enjoy sir")
                os.startfile("C:\\Users\\SANU\\Downloads\\music\\broken angel.mp3")
            elif "Paradise" in query:
                speak("here is your song , enjoy sir")
                os.startfile("C:\\Users\\SANU\\Downloads\\music\\paradise.mp3")
            elif "sorry" in query:
                speak("here is your song , enjoy sir")
                os.startfile("C:\\Users\\SANU\\Downloads\\music\\sorry.mp3")
            elif "Breaking the rules" in query:
                speak("here is your song , enjoy sir")
                os.startfile("C:\\Users\\SANU\\Downloads\\music\\breaking the rules.mp3")

        elif "screenshot" in query:
            speak("ok sir , from what name do you want to save it")
            path = takecommand()
            speak("")
            path1name = path + ".png"
            path1 = "C:\\Users\\SANU\\PycharmProjects\\JARVIS\\screenshot\\" + path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            speak("done sir")

        elif "show me that pic" in query:
            os.startfile("C:\\Users\\SANU\\PycharmProjects\\JARVIS\\screenshot")
            speak("here is you screenshot")

        elif "sad" in query or "upset" in query:
            speak("what happened sir , may i do something for you")

        elif "happy" in query:
            speak("i am pleased to know that sir")
            speak("i am also happy for you")

        elif "stressed" in query:
            speak("ok sir , i will play something to relax you")
            os.startfile("C:\\Users\\SANU\\Downloads\\music\\sorry.mp3")

        elif "suggest" in query:
            speak("what kind of suggestion you want sir")
            takecommand()
            speak("ofcourse sir i would love to help you in that")
            speak("i think you should wear white shirt with black pant, that would be the best combination sir")

        elif "weather" in query:
            speak("Its beautiful morning in Daltonganj")
            speak("Weather is clear , Sun is bright")
            speak("its perfect day to start sir")

        elif "open map" in query:
            speak("which place do you want to search")
            query = takecommand()
            web2 = 'http://www.google.com/maps/place/' + query
            webbrowser.open(web2)
            speak("here is your result sir")

        elif "close map" in query:
            os.system(f"TASKKILL /f /im chrome.exe")

        elif "activate how to do mode" in query:
            speak("how to do mode is activated")
            from pywikihow import search_wikihow
            while True:
                speak("tell me what do you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, how to mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this!")

        elif "temperature" in query:
            search = "temperature in daltonganj"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_="BNeawe").text
            speak(f"the temperature outside is {temperature} ")

        elif 'go' in query:
            speak("ok sir , you can call me anytime.")
            exit()




