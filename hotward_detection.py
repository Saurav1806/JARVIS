import os
import speech_recognition as sr


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listesning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}")

    except Exception as e:
        return "None"
    return query.lower()

while True:

    wake_up = takecommand()

    if "wake up" in wake_up:
        os.startfile("C:\\Users\\SANU\\PycharmProjects\\JARVIS\\JARVIS.py")

    else:
        print("Nothing...")

