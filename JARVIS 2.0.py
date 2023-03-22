import ctypes
import datetime
import os
import smtplib

import pyjokes
import pyttsx3
import speech_recognition as sr
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Jarvis 2 point o")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("How can i Help you, Sir")
    print("How can i Help you, Sir")


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
        speak("Unable to Recognize your voice. say that again sir")
        print("Unable to Recognize your voice.Say that again sir.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    #Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()





if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        if "what is your name" in query:
            speak("My friends call me , jarvis 2 point o Sir")
            print("My friends call me , jarvis 2 point o Sir")

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            print("I'm not sure about, may be you should give me some time")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif "also fine" in query or "good" in query:
            speak("It's good to know that your fine")

        elif "i love you" in query:
            speak("I love u too Sir")
            print("I love u too Sir")

        elif "some chat" in query or "some talk" in query:
            speak("on what topic you want to have chat sir")
            print("on what topic, you want to have chat sir.")
            takeCommand()
            speak("sure sir , i would love to discuss on that")
            print("sure sir , i would love to discuss on that")
            takeCommand()
            speak("ok sir As you want")
            print("ok sir As you want")


        elif "what is" in query or "who is" in query:

            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
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

        elif "don't listen" in query or "stop listening" in query:
            speak("Ok sir i am going to quit.")
            a = int(takeCommand())
            datetime.time.sleep(a)


        elif "who i am" in query:
            speak("If you talk then definitely your human.")
            print("If you talk then definitely your human.")

        elif "this world" in query:
            speak("Thanks to Saurav. further It's a secret")
            print("Thanks to Saurav. further It's a secret")


        elif "who are you" in query:
            speak("I am your virtual assistant created by Saurav")
            print("I am your virtual assistant created by Saurav")

        elif "reason for you" in query:
            speak("I was created as a Minor project by Mister Saurav ")
            print("I was created as a Minor project by Mister Saurav ")

        elif "are you there" in query:
            speak("Yes sir i am here , sorry for interupt Sir , how can i help you sir")
            print("Yes sir i am here , sorry for interupt Sir , how can i help you sir")

        elif "calculate" in query:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

        elif "who is my favourite teacher" in query:
            speak("Sir , as you told me D B M S is your favourite Subject")
            print("Sir , as you told me D B M S is your favourite Subject")
            speak("so i think , its Vaishali Maam.")
            takeCommand()
            speak("I know sir , she is excellent teacher as well as great mentor also")
            print("I know sir , she is excellent teacher as well as great mentor also")
            takeCommand()
            speak("I would like to meet her someday sir")
            print("I would like to meet her someday sir")
            takeCommand()
            speak("Thank You sir")
            print("Thank You sir")






