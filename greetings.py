import datetime
import speak as spk
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        spk.speak("Good Morning")
    elif hour >= 12 and hour < 18:
        spk.speak("Good Afternoon")
    else:
        spk.speak("Good Evening")
    # spk.speak("Hey buddy, How can I Help you?")