import cv2
import pyautogui
import datetime

def takePhoto():
    strt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    cam = cv2.VideoCapture(0)
    s, img = cam.read()
    if s:
        cv2.destroyWindow("cam-test")
        cv2.imwrite("C:\\Users\\haPPy\\OneDrive\\Pictures\\Camera Roll\\IMG"+strt+'.jpg',img)
def takeScreenshot():
    strt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    scr = pyautogui.screenshot()
    scr.save(r'C:\\Users\\haPPy\\OneDrive\\Pictures\\Screenshots\\IMG'+strt+'.png')