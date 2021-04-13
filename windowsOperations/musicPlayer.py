import os
import random
def playMusic():
    music_dir = "C:\\Users\\haPPy\\Music"
    music = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, music[random.randrange(len(music)-1)]))
