import os
import wmi
from win32com.client import GetObject
objWMI = GetObject('winmgmts:\\\\.\\root\\WMI').InstancesOf('WmiMonitorBrightness')

# with keyboard.pressed(Key.):
#     keyboard.press('a')
#     keyboard.release('a')
for obj in objWMI:
    if obj.CurrentBrightness != None:
        # print("CurrentBrightness:" + str(obj.CurrentBrightness))
        brightness = int(obj.CurrentBrightness)
def adjustBrightness(query):
    global brightness
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)
    print(c.WmiM)
    # print(brightness)
    if 'increase' in query:
        if brightness != 100 and brightness + 30 <= 100:
            brightness+=30
    elif 'decrease' in query:
        if brightness != 0 and brightness - 30 >= 0:
            brightness-=30
    
