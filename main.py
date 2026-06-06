import speech_recognition as sr
import requests
import os
from dotenv import load_dotenv
import replicate

load_dotenv()
api=os.getenv("apikey")

def voiceinput(t=12,p=25):
    with sr.Microphone() as source :
        print("listening...")
        audio=rec.listen(source,timeout=t,phrase_time_limit=p)
    return rec.recognize_google(audio)

def prompt(text):
    return f"""
    Create a highly detailed, visually stunning image based on the following description: {text}.

    The image should be:
    - ultra realistic and cinematic
    - highly detailed with sharp focus
    - professionally composed like a DSLR photograph
    - with proper lighting, depth, and perspective
    - 4K high resolution quality
    - visually clear and meaningful even if the input is abstract

    If the input is abstract or unclear, creatively interpret it into a meaningful and artistic visual scene.
    """.strip()

if __name__=='__main__':
    rec=sr.Recognizer()
    print("Initialising...")
    try:
        print("Listening...")
        uservoice=voiceinput()
        print(uservoice)
        img_prompt=prompt(uservoice)
    except Exception as e:
        print("Retry")