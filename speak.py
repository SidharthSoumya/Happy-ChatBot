from gtts import gTTS
import os
import playsound

def speak(audio):
    tts = gTTS(text=audio , lang='en-in')
    tts.save("demo.mp3")
    # os.system("demo.mp3")
    playsound.playsound("demo.mp3", False)
    os.remove("demo.mp3")
