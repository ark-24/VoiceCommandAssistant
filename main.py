import speech_recognition as sr
import io
from gtts import gTTS
from tempfile import TemporaryFile
from IPython.display import Audio
import time
import pyttsx3

r = sr.Recognizer()
def speak():
    engine = pyttsx3.init()
    engine.say("how can i assist you?")
    engine.runAndWait()


while True:
    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r.listen(mic)
            message = r.recognize_google(audio)
            print(message)
            if message == "hello Bob":
                speak()
    
        
        
    except sr.UnknownValueError():
        r = sr.Recognizer()
        continue



