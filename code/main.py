#!/usr/bin/env python

import cv2 # to process the images
import pyautogui as pag # to handle mouse movements
import pygetwindow as gw # to grab screenshots of My Singing Monsters window
from PIL import Image
import time
"""
STRATEGY:

user has to enter the memory game and clear any pop ups, then run the script

script will go one level by one, and initially will parse through each tile and screenshot each consecutive pair until all pairs have been recoreded.
then will use cv2 to parse each screenshot and store the locations of the two monsters
once each screenshot has been parsed, it will




"""

path = 'C:\\Users\\ethan\\Documents\\Code\\msm-matching-automation\\media\\test.png'

window = gw.getWindowsWithTitle('Snip & Sketch')[0]
window.activate()
time.sleep(0.1)
left, top = window.topleft
right, bottom = window.bottomright

pag.screenshot(path)
img = Image.open(path)
img = img.crop((left, top, right, bottom))
print(left, top, right, bottom)
#img.save(path)
#img.show(path)

# can probably use try to click every tile and count the numbers of tile clicked instead of saving tiles on each level

test = pag.locateAllOnScreen('C:\\Users\\ethan\\Documents\\Code\\msm-matching-automation\\media\\tile.png', confidence=0.5)
print("after")
#window = gw.getWindowsWithTitle('My Singing Monsters')[0]
#window.activate()
for pos in list(test):
    print(pos)
    pag.moveTo(x=pos.left - pos.width/2, y=pos.top - pos.height/2)
    time.sleep(1)