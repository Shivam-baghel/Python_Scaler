import pyautogui as pag
import time
import random
pag.FAILSAFE = False
while True:
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    pag.click()
    time.sleep(10)