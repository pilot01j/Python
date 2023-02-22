import pyautogui
import time
import keyboard
import win32api, win32con

time.sleep(1)
jumps = 0
# Use PyWin32 for Fast Keyboard Press Response
def jump():
    global jumps
    win32api.keybd_event(38, 0, 0, 0)
    time.sleep(0.01)
    win32api.keybd_event(38, 0, win32con.KEYEVENTF_KEYUP, 0)
    jumps += 1


def kneel():
    win32api.keybd_event(40, 0, 0, 0)
    time.sleep(0.4)
    win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
    print("Pterodactyl")


# Press 'q' to stop running
# Finding and Selecting Particular Pixcels and RGB with PyAutoGUI
# Modify Logic to Adjust with Faster Speed
while not keyboard.is_pressed('q'):
    if pyautogui.pixel(730, 468)[0] == 83:
        jump()
        print("Tall cactus!")
    elif pyautogui.pixel(715, 490)[0] == 83:
        jump()
        print("Short cactus!")
    if pyautogui.pixel(760, 460)[0] == 83:
        kneel()

    # verify if speed increases
    if jumps > 3:
        if pyautogui.pixel(720, 468)[0] == 83:
            jump()
            print("Tall cactus!")
        elif pyautogui.pixel(705, 490)[0] == 83:
            jump()
        if pyautogui.pixel(750, 460)[0] == 83:
            kneel()
