import speech_recognition as sr
from googletrans import Translator

def listen():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source,0,4)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="hi").lower()
    except:
        return ""
       
    return query 

#Translation

def Translate(Text):
    # line = str(Text)
    translate = Translator()
    result = translate.translate(Text)
    data = result.text
    print(f"You : {data.upper()}.") 
    return data

#speak

import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    print("")
    print(f"AI : {Text.upper()}.")
    print("")
    engine.say(Text)
    engine.runAndWait()



#MicConnect

def MicConnect():
    query = listen()
    data = Translate(query)
    Speak(data)
    # return data

MicConnect()