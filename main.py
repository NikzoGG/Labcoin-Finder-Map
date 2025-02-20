import pyautogui
import requests
import numpy 
import pygame
from time import sleep

#RUN THE SCRIPT WITH TINYTASK RESETTING THE LABCOIN APP SO THE COIN CAN EVENTUALLY POP UP ON THE SCREEN
#RUN THE SCRIPT WITH TINYTASK RESETTING THE LABCOIN APP SO THE COIN CAN EVENTUALLY POP UP ON THE SCREEN
#RUN THE SCRIPT WITH TINYTASK RESETTING THE LABCOIN APP SO THE COIN CAN EVENTUALLY POP UP ON THE SCREEN
#REMOVE THE # INFRONT OF THE FOUND SOUND LINES IF YOU WANT TO START A LOUD SOUND WHEN A COIN IS DETECTED
#IF THE SCRIPTS HAS SOMETHING PURPLE IN THE CODE SCROLL DOWN SO IT DOESNT SEE IT BECAUSSE IT MIGTH DETECT ITT AS A COIN

pygame.init()
pygame.mixer.init()

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1338846147837694012/gxPUy1ghZks5XV0RLV5drXk1qcDbfUMCXvxYRgvvkxR1-oau6PSkm40hPLwa0VWXTljW"

def sendmessage(content):
    data = {"content": content}
    requests.post(DISCORD_WEBHOOK_URL, json=data)

#found_sound = pygame.mixer.Sound("sound.mp3")
#found_sound.set_volume(0.04)
TARGET_COLOR = (117,58,149)




TOLERANCE = 10  

def find_color_on_screen(target_color, tolerance=0):
    
    screenshot = pyautogui.screenshot()

   
    screenshot_array = numpy.array(screenshot)

   
    matches = numpy.where(
        (numpy.abs(screenshot_array[:, :, 0] - target_color[0]) <= tolerance) &
        (numpy.abs(screenshot_array[:, :, 1] - target_color[1]) <= tolerance) &
        (numpy.abs(screenshot_array[:, :, 2] - target_color[2]) <= tolerance)
    )

    
    if matches[0].size > 0:
        return list(zip(matches[1], matches[0]))  
    return []

def main():
    colorfound = False
    print("Starting color scan...")
    try:
        while True:                      
            coordinates = find_color_on_screen(TARGET_COLOR, TOLERANCE)
            if coordinates:
                #found_sound.play()
                for l in range(25):
                    sendmessage("ПУСНАХА ПУБЛИЧЕН ЛАБКОЙН В ПРИЛОЖЕНИЕТО!!!")
                print("Color found")
                colorfound = True
                break
            else:
                print("Color not found.")
                pass
            

            sleep(1)
    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()
























