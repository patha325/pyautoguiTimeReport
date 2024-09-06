import subprocess
import pyautogui
import time
import sys
 
 
def main():
    factor = 1
    if sys.platform == "linux" or sys.platform == "linux2":
        subprocess.run(["google-chrome", "--app-url", "https://copernicus.scania.com/"])
    elif sys.platform == "darwin":
        subprocess.run(["open", "-a", "Microsoft Teams classic.app"])
        factor = 2
    elif sys.platform == "win32":
        print(":(")
 
    time.sleep(2)
    for step in range(3):
        print(f"step {step}")
        found = pyautogui.locateCenterOnScreen(f'stepdnd{step}.png', confidence=0.70)
        if found:
            print(f"Icon found at {found}. Clicking now...")
            pyautogui.moveTo(found[0] // factor, found[1] // factor, duration=0.2)
            pyautogui.click()
            time.sleep(2)
 

if __name__ == '__main__':
    main()