import pyautogui
from PIL import ImageGrab
import time



def press(key):
    pyautogui.press(key)
    time.sleep(.01)


def restart():
    time.sleep(3)
    #725, 244
    pyautogui.click(x=721, y=400)


def collision(data):
    #bird area range, check if grey. check area first by drawing data[i,j]=0
    for i in range(970, 1050):
        for j in range(560, 600):
            if data[i,j] < 100:
                press("down")
                return

    #cactus area, check if dark grey
    for i in range(970, 1255):
        for j in range(795, 865):
            if data[i,j] < 100:
                press("space")
                return
    return
restart()
while True:
    # grab image in box, mode L is greyscale
    image = ImageGrab.grab().convert('L')
    data = image.load()

    collision(data)



