import pyautogui
import numpy 
import pygame
from time import sleep

pygame.init()
pygame.mixer.init()

found_sound = pygame.mixer.Sound("sound.mp3")
found_sound.set_volume(0.08)
TARGET_COLOR = (182, 88, 205)  

#Za publichni cveta
#182,88,205


 


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
                found_sound.play()
                print("Color found")
                colorfound = True
            else:
                print("Color not found.")
                pass
            
            if colorfound == True:
                seenthing = input("Vidq li koina otgovori za da spresh zvuka/da/ ")
                if seenthing == "da":
                    break

            sleep(1)
    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()

