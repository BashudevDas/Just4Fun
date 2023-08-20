import pyautogui #A GUI automation Python module
import time
time.sleep(10)#a temporaryb time-lapse to allow the user to select a platform for the desired text to be written
count = 0

while count <=100: #Mention the number of times the text needs to be written
    pyautogui.typewrite("") # mention the text you want to send multiple times
    pyautogui.press("enter")
    count+=1
