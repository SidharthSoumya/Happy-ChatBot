# from gtts import gTTS
import pyttsx3

def speak(audio):
    engine = pyttsx3.init()

    # Changing the voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-1].id)

    # Setting up the speed of the voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)

    # Play the audio
    engine.say(audio)

    engine.runAndWait()
