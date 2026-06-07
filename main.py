import speech_recognition as sr
import requests
import os
from dotenv import load_dotenv
import webbrowser as wb

load_dotenv()
os.environ["REPLICATE_API_TOKEN"]=os.getenv("apikey")

def voiceinput(t=12,p=25):
    with sr.Microphone() as source :
        print("listening...")
        audio=rec.listen(source,timeout=t,phrase_time_limit=p)
    return rec.recognize_google(audio)

def image():
    pass

def prompt(text):
    return f"""
    Create a highly detailed, visually stunning image based on: {text}.
    ultra realistic, cinematic lighting, high resolution,
    professional composition, depth of field.
    """.strip()

if __name__=='__main__':
    rec=sr.Recognizer()
    print("Initialising...")
    try:
        uservoice=voiceinput()
        print(uservoice)
        img_prompt=prompt(uservoice)
        image(img_prompt)
    except Exception as e:
        print("Retry")