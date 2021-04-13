# from gtts import gTTS
import pyttsx3
import os
import playsound

def speak(audio):
    engine = pyttsx3.init()
    # tts = gTTS(text=audio , lang='en-in')
    # tts.save("demo.mp3")
    # os.system("demo.mp3")
    # voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(voice.id)
    #     engine.setProperty('voice', voice.id)  # changes the voice
    #     engine.say('The quick brown fox jumped over the lazy dog.')
    engine.say(audio)
    engine.runAndWait()
    # playsound.playsound("demo.mp3", False)
    # os.remove("demo.mp3")
