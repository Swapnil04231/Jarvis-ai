import datetime

import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
from config import apikey
import random


from speech_recognition.recognizers import google

def ai(prompt):
    openai.api_key = apikey
    text=f"Open ai response for prompt {prompt}\n**************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    print(response[0]["text"])
    text=response[0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open (f"openai/prompt -{random.randint(1,100)}", "w") as file:
        file.write(text)






def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said :{query}")
            return query
        except Exception as e:
            return "Some error occured . Sorry from swapnil "


if __name__=='__main__':
    print("PYcharm")
    say("Hello I am Swapnil's AI")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo:add more sites
        sites=[["youtube","youtube.com"],["wikipedia","wikipedia.com"],["google","google.com"],["facebook","facebook.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say("Opening {site[0]}")
                webbrowser.open(site[1])

        #if "open music" in query:
            #say("Opening music")
            #musicpath= "Users\swapn\Downloads\future-design-344320.mp3"
            #os.system(f"open  {musicpath}")

        if "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            seconds = datetime.datetime.now().strftime("%S")
            say(f" Now time is {hour} bej ke {minute} minute or {seconds} second")

        # if "open camera" in query:

        #if "open visual studio".lower() in query.lower():
           # os.system("C:/Users/swapn/OneDrive/Desktop/Visual Studio Code.lnk")

        if "Artificial intelligence".lower() in query.lower():
            ai(prompt=query)







        #say(query)












