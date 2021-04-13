import os
from pynput.keyboard import Key, Controller
import win32com.client

keyboard = Controller()
def openBuild(query):
    if 'run' and 'frcs' in query:
        os.chdir("D:\\FRCS\\Trunk\\Frontend\\frcs")
        WshShell = win32com.client.Dispatch("WScript.Shell")
        # WshShell.run("cmd")
        WshShell.run("ng serve --open")
def makeBuild(query):
    if 'build' and 'frcs' in query:
        os.chdir("D:\\FRCS\\Trunk\\Frontend\\frcs")
        WshShell = win32com.client.Dispatch("WScript.Shell")
        WshShell.run("ng build")

        
        
        