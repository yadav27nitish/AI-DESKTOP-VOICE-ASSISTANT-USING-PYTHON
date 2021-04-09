import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
# sapi5 is help to take voice from window. it take inbuilt voice from window which is provided by microsoft.
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    # this function helps to speak the voice
    engine.say(audio)
    engine.runAndWait()
    # Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hey I am Sivi. How may i help you.")


def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # this line wait for listening till 1 sec in case someone is not speak
        audio = r.listen(source)
    try:
         # In case sivi is not able to understand.
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

if __name__ == "__main__":
    wishMe()
    #while (True):
    query = takecommand()
    if 'Wikipedia' or 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open Youtube' or 'youtube' or 'YouTube' in query:
        webbrowser.open("youtube.com")
    elif 'Google' or 'google' in query:
        webbrowser.open("google.com")
    elif 'Play music' or 'play music' or 'Play Music' in query:
        webbrowser.open("youtube.com")
    elif 'Time' or 'time' in query:
        c_time = datetime.datetime.now()
        speak(f"Time is {c_time}")
