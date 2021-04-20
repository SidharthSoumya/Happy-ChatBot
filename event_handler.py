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

query_g = ''
def time():
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    spk.speak("It is")
    spk.speak(strtime)
    print(strtime)

def play():
    player.playMusic()

def search_wiki():
    global query_g
    spk.speak('Searching Wikipedia...')
    query_g = query_g.replace("wikipedia", "")
    res = ''
    res = wikipedia.summary(query_g, sentences=2)
    spk.speak("According to wikipedia")
    spk.speak(res)

def search_browser():
    query = query_g.replace('search', '')
    # query = query.replace('happy', '')
    query = query.replace('for', '')
    browser.searchString(query)

def vs_code():
    code_path = "C:\\Users\\haPPy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    # code_path = "C:\Users\haPPy\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    os.startfile(code_path)

def py_charm():
    code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.5\\bin\\pycharm64.exe"
    os.startfile(code_path)

def screen_brightness():
    so.adjustBrightness(query_g)

def photo_capture():
    cm.takePhoto()

def screenshot_capture():
    cm.takeScreenshot()

def quit():
    exit()

def default():
    pass

def handle_event(query):
    global query_g
    query_g = query
    switcher = {
        'time': time,
        'play music': play,
        'change music': play,
        'wikipedia': search_wiki,
        'search': search_browser,
        'code': vs_code,
        'brightness': screen_brightness,
        'take photo': photo_capture,
        'take screenshot': screenshot_capture,
        'py charm': py_charm,
        'exit': quit
    }
    for key in switcher.keys():
        if query.find(key) == -1:
            default()
        else:
            switcher[key]()
            break