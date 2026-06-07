import os
import speech_recognition as sr
from huggingface_hub import InferenceClient
from dotenv import load_dotenv


load_dotenv(".env")
api=os.getenv("apikey")

client=InferenceClient(token=api)
img_model="stabilityai/stable-diffusion-xl-base-1.0"


def voiceinput(timeout=20, phrase_time_limit=80):
    try:
        with sr.Microphone() as source:
            print("Listening... speak now.")
            audio = rec.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        text = rec.recognize_google(audio)
        return text
    except Exception as e:
        print("Voice recognition failed:", e)
        return None


def prompt(text):
    return f"""
    Ultra realistic cinematic image of {text},highly detailed, professional photography,
    sharp focus, dramatic lighting,depth of field, vibrant colors,
    4k quality, realistic textures,masterpiece composition, visually stunning"""


def image(prompt_text):
    print("Generating...")
    try:
        img = client.text_to_image(prompt_text,model=img_model)
        print("Image generated successfully")
        img.show()
    except Exception as e:
        print("Generation failed:", e)

if __name__=="__main__":
    rec=sr.Recognizer()
    print("Initialising...")
    try:
        uservoice=voiceinput()
        print(uservoice)
        img_prompt=prompt(uservoice)
        image(img_prompt)
    except Exception as e:
        print("Retry")


# A majestic dragon flying above snow-covered mountains during a thunderstorm,
# lightning striking in the background, glowing blue eyes, ultra realistic scales,
# cinematic fantasy scene, volumetric clouds, dramatic lighting, highly detailed, 8k masterpiece