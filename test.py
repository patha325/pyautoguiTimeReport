import subprocess
import pyautogui
import time
import webbrowser
import sys
import pytesseract
import cv2
from PIL import Image
import os

from donotRead import pv
 

def ocr (imgpath):
    im = cv2.imread(imgpath)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    tmpfile = "gray_numbers.jpg"
    cv2.imwrite(tmpfile, gray)
    text = ''.join(filter(lambda x: x.isdigit(), pytesseract.image_to_string(Image.open(tmpfile))))
    if len(text) == 6:
        print(text)
        return text
    return "??????"

def FindAndClick(icon_path):
    # Time interval (in seconds) between each search for the icon
    search_interval = 1
    found = None
    while not found:
        # Attempt to locate the icon on the screen
        found = pyautogui.locateCenterOnScreen(icon_path, confidence=0.80) # Adjust confidence as needed
        if found:
            print(f"Icon found at {found}. Clicking now...")
            #time.sleep(1)
            #import pdb; pdb.set_trace()
            pyautogui.moveTo(found[0]/2, found[1]/2, duration=1) 
            pyautogui.click()#(found)
        
        else:
            print("Icon not found, waiting and trying again...")
            time.sleep(search_interval)

def Copernicus():
    factor = 1
    if sys.platform == "linux" or sys.platform == "linux2":
        subprocess.run(["google-chrome", "--app-url", "https://copernicus.scania.com/"])
    elif sys.platform == "darwin":
        subprocess.run(["open", "-a", "Google Chrome", "https://copernicus.scania.com/"])
        factor = 2
    elif sys.platform == "win32":
        print(":(")
 
    time.sleep(5)
    for step in range(3):
        #
        print(f"step {step}")
        found = pyautogui.locateCenterOnScreen(f'step{step}.png', confidence=0.70)
        if found:
            print(f"Icon found at {found}. Clicking now...")
            pyautogui.moveTo(found[0] // factor, found[1] // factor, duration=0.2)
            pyautogui.click()
            time.sleep(2)
 
    pyautogui.press('tab')
    for i in range(5):
        pyautogui.press('8')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1)
 
    for step in range(3,5):
        #
        print(f"step {step}")
        found = pyautogui.locateCenterOnScreen(f'step{step}.png', confidence=0.70)
        if found:
            print(f"Icon found at {found}. Clicking now...")
            pyautogui.moveTo(found[0] // factor, found[1] // factor, duration=0.2)
            time.sleep(0.2)

def PulseSecure():
    # Use the 'open' command to launch Microsoft Teams
    # The '-a' option specifies the application to open
    subprocess.run(["open", "-a", "Pulse Secure.app"])
 
    time.sleep(1)
 
    # Path to the screenshot of the icon you want to click on
    icon_path = '/Users/phaond/Downloads/capyCrew/part1.png'
    FindAndClick(icon_path)

    time.sleep(3) #Waiting for window

    #Choose sms
    icon_path = '/Users/phaond/Downloads/capyCrew/part2.png'
    FindAndClick(icon_path)

    time.sleep(1)
    
    #Connect
    icon_path = '/Users/phaond/Downloads/capyCrew/part3.png'
    FindAndClick(icon_path)

    time.sleep(1)

    pyautogui.write('phaond') 
    pyautogui.press('tab')
    pyautogui.write(pv) 

    #time.sleep(2)

    #Connect with username and password
    icon_path = '/Users/phaond/Downloads/capyCrew/part4.png'
    FindAndClick(icon_path)

    #Open chrome and get sms

    time.sleep(5)
    webbrowser.get('chrome').open_new_tab("https://messages.google.com/web/conversations")

    time.sleep(2)
    #Find PHX
    #icon_path = '/Users/phaond/Downloads/capyCrew/part5.png'
    #FindAndClick(icon_path)

    time.sleep(3)

    center = pyautogui.locateOnScreen('/Users/phaond/Downloads/capyCrew/part5.png')
    im = pyautogui.screenshot(region=(int(center[0]/2),int(center[1]/2), 100, 50))
    im.save("/Users/phaond/Downloads/capyCrew/screenshot.png")

    time.sleep(1)

    oneTimeCode = ocr("/Users/phaond/Downloads/capyCrew/screenshot.png")

    icon_path = '/Users/phaond/Downloads/capyCrew/part6.png'
    FindAndClick(icon_path)

    pyautogui.write(oneTimeCode) 

    icon_path = '/Users/phaond/Downloads/capyCrew/part7.png'
    FindAndClick(icon_path)

if __name__ == "__main__":

    PulseSecure()
    time.sleep(30)
    Copernicus()

    time.sleep(10)

    # Specify the path to your image
    image_path = '/Users/phaond/Downloads/capyCrew/crew.png'
 
    # Convert the image path to a URL
    image_url = 'file://' + os.path.abspath(image_path)
 
    # Use the default browser to open the image URL
    webbrowser.get('chrome').open(image_url)