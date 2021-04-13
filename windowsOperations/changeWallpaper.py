import ctypes
import os
import random

def change():
    wallpaperDir = "C:\\Users\\haPPy\\OneDrive\\Pictures\\Wallpapers"
    wallpaperList = os.listdir(wallpaperDir)
    print(wallpaperList)
    wPath = wallpaperDir+'\\' + \
        wallpaperList[random.randrange(len(wallpaperList)-1)]
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wPath, 0)
