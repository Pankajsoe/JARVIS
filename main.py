import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
recognizer = sr.recognizers
engine = pyttsx3.init()
newsapi = "27487455ad33474b98e3244bc052b44a"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the music file 
    pygame.mixer.music.load("temp.mp3")

    # Play the music
    pygame.mixer.music.play()

    # Keep the script running to let the music play
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove

def aiProcess(command):
    client = OpenAI(api_key="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")
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "You are a virtual assistant names jarvis skilled in general task like alexa"}
       , {"role" : "user", "content" : command}
    ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=27487455ad33474b98e3244bc052b44a")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles 
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let open ai handle the request
        output = aiProcess(c)
        speak(output)
        
        
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    
    while True:
        # Listen for the wake word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active !")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

                    
        except Exception as e:
            print("error; {0}".format(e))

