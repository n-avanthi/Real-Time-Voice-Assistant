import os
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

load_dotenv()
recognizer = sr.Recognizer()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def listen_microphone():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        txt = recognizer.recognize_google(audio)  # Using Google Speech Recognition
        print("You said:", txt)
        return txt
    except sr.UnknownValueError:
        print("Sorry, could not understand audio. Please repeat")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def generate_content(listen):
    if listen:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(listen)
        # generated_text = response.text[:150]
        print(response.text)
        return(response.text)
    else:
        return "Sorry, Could not understand audio, Please repeat"

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
        
while True:
    listen = listen_microphone()
    if listen and listen.lower() == 'exit':
        break
    else:
        generated_text = generate_content(listen)
        text_to_speech(generated_text)
