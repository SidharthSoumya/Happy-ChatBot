import webbrowser
import wikipedia
import os
import datetime
import random
import greetings as gr
import speak as spk
import shutil
import recogniseSpeech as rs
import windowsOperations.openInChrome as browser
import windowsOperations.changeWallpaper as cw
import windowsOperations.musicPlayer as player
import windowsOperations.angular as ng
import windowsOperations.camera as cm
import windowsOperations.screenOperaion as so

if __name__ == '__main__':
    # gr.greet()
    cTime=datetime.datetime.now().minute
    while 1:
        query = rs.takeCommand().lower()
        print(datetime.datetime.now().minute)

        if datetime.datetime.now().minute < cTime+1 or ('happy' in query):
            cTime = datetime.datetime.now().minute
            if 'wikipedia' in query:
                spk.speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                spk.speak("According to wikipedia")
                spk.speak(results)
            elif 'browser' in query or 'open' in query:
                browser.openURL(query)
            elif 'search' in query:
                query = query.replace('search', '')
                query = query.replace('happy', '')
                query = query.replace('for', '')
                browser.searchString(query)
            elif 'play music' in query:
                player.playMusic()

            elif 'time' in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                spk.speak("It is")
                spk.speak(strtime)
                print(strtime)

            elif 'code' in query:
                code_path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
                # code_path = "C:\\Users\\Soumya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)
            elif 'change wallpaper' in query:
                cw.change()
            elif 'run frcs' in query:
                ng.openBuild(query)
            elif 'brightness' in query:
                so.adjustBrightness(query)
            elif 'build frcs' in query:
                ng.makeBuild(query)
            elif 'quit' in query:
                spk.speak("thank you")
            elif 'clear screen' in query:
                os.system("cls")
                spk.speak("The screen is cleared")
            elif 'copy file' in query:
                shutil.copytree(r'F:\\python\\Programs\\Voice Assistant\\happy.py', r'\\192.168.0.1\\MyShare\\Sidharth')
            elif ('take' and 'photo') in query:
                cm.takePhoto()
            elif ('take' and 'screenshot') in query:
                cm.takeScreenshot()
            elif 'thank you' in query:
                spk.speak('You are welcome Sir !')
            else:
                print("Thank You")
