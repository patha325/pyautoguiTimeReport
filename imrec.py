import cv2
import pyautogui
import time
import webbrowser


webbrowser.get('chrome').open_new_tab("https://messages.google.com/web/conversations")

time.sleep(3)

center = pyautogui.locateOnScreen('/Users/phaond/Downloads/capyCrew/part5.png')
im = pyautogui.screenshot(region=(int(center[0]/2),int(center[1]/2), 100, 50))
im.save("/Users/phaond/Downloads/capyCrew/screenshot.png")

time.sleep(2)

#cv2.imshow("Sheep", im)