import pyautogui
import time
import sys
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = None
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])
    
print("started")
while(True):
    x=0
    while(x<numMin):
        time.sleep(60)
        x+=1
    for i in range(0,3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))
