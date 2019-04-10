import cv2, random, time
from pynput import keyboard
from random import randint
from pyclick import HumanClicker
import pyautogui




def random_movement(x_min, y_min):                                                                                   ## movement 1st spot

    x = randint(x_min, x_min + 13)                                                                                   ## + random possible deviation
    y = randint(y_min-12 , y_min)

    return hc.move((x,y), random.uniform(0.2,1))

def inventory_click(x_min_2,y_min_2):                                                                                ## movement to 2nd spot

    x2 = randint(x_min_2, x_min_2 +20)                                                                               ## + random possible deviation
    y2 = randint(y_min_2 -20 , y_min_2)

    return hc.move((x2,y2), random.uniform(0.2,1))

def on_press(key):                                                                                                   ## Script disabler function
    global break_program
    if key == keyboard.Key.f12:
        print('Closing program')
        break_program = True
        return False





client_location = pyautogui.locateOnScreen('D:\pyhton files\autoclicker\sampleclient.png', confidence=0.8)     ## Makes screenshot of screen and compares it with sample image
print('Coordinates of client are: ' + str(client_location))

client_center = pyautogui.center(client_location)                                                                   ## Finds center coordinates of found client
print('Center of client is: ' + str(client_center))

pyautogui.moveTo(client_center[0] , client_center[1]+ 300)                                                          ## Selects window and by clicking and prepares menu
pyautogui.click()
pyautogui.press('f6')

hc = HumanClicker()                                                                                                 ## Initialising the Human-like movement

x_min = client_center[0] + 327                                                                                      ## Locations of clickables and 2nd location relative to the center of client
y_min = client_center[1] - 40
x_min_2 = client_center[0] + 307
y_min_2 = client_center[1] - 10


while True:

    break_program = False
    with keyboard.Listener(on_press=on_press) as listener:
        while break_program == False:

            print('Moving...')                                                                                       ## Keylistener to disable script after pressing F12
            random_movement(x_min,y_min)
            pyautogui.click()
            delay = random.uniform(0,0.2)                                                                            ## Randomised extra delays
            print('Waiting ' + str(round(delay,3)) + ' seconds to avoid detection' )
            time.sleep(delay)

            delay2 = random.uniform(0,0.46)
            time.sleep(delay2)
            print('Waiting ' + str(round(delay2,3)) + ' seconds to avoid detection' )
            inventory_click(x_min_2, y_min_2)
            pyautogui.click()
            print('Waiting for alc + delay...')
            time.sleep(3 + random.uniform(0,0.5))
            pyautogui.press('f6')

    break
    listener.join()
