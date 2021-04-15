import wikipedia
import os
import speak as spk
import windowsOperations.openInChrome as browser
import windowsOperations.changeWallpaper as cw
import windowsOperations.musicPlayer as player
import windowsOperations.angular as ng
import windowsOperations.camera as cm
import windowsOperations.screenOperaion as so
import shutil
import datetime

def time():
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    spk.speak("It is")
    spk.speak(strtime)
    print(strtime)
def play():
    player.playMusic()

def default():
    print("Thank You")

def handle_event(query):
    switcher = {
        'time': 'time',
        'play': 'play'
    }
    switcher.get(query, default)()
    # if 'wikipedia' in query:
    #     spk.speak('Searching Wikipedia...')
    #     query = query.replace("wikipedia", "")
    #     results = wikipedia.summary(query, sentences=2)
    #     spk.speak("According to wikipedia")
    #     spk.speak(results)
    # elif 'search' in query:
    #     query = query.replace('search', '')
    #     query = query.replace('happy', '')
    #     query = query.replace('for', '')
    #     browser.searchString(query)
    # elif 'play music' in query or 'change music' in query:
    #     player.playMusic()
    #
    # elif 'time' in query:
    #     strtime = datetime.datetime.now().strftime("%H:%M:%S")
    #     spk.speak("It is")
    #     spk.speak(strtime)
    #     print(strtime)
    #
    # elif 'code' in query:
    #     # code_path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
    #     code_path = "C:\\Users\\haPPy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    #     # code_path = "C:\Users\haPPy\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    #     os.startfile(code_path)
    # elif 'change wallpaper' in query:
    #     cw.change()
    # elif 'run frcs' in query:
    #     ng.openBuild(query)
    # elif 'brightness' in query:
    #     so.adjustBrightness(query)
    # elif 'build frcs' in query:
    #     ng.makeBuild(query)
    # elif 'quit' in query:
    #     spk.speak("thank you")
    # elif 'clear screen' in query:
    #     os.system("cls")
    #     spk.speak("The screen is cleared")
    # elif 'copy file' in query:
    #     shutil.copytree(r'F:\\python\\Programs\\Voice Assistant\\happy.py', r'\\192.168.0.1\\MyShare\\Sidharth')
    # elif ('take' and 'photo') in query:
    #     cm.takePhoto()
    # elif ('take' and 'screenshot') in query:
    #     cm.takeScreenshot()
    # elif 'thank you' in query:
    #     spk.speak('You are welcome Sir !')
    # else:
    #     print("Thank You")