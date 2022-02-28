import speech_recognition as sr
import time
from glob import glob
import pygame
import os
import pyttsx3

pygame.init()

gameDisplay = pygame.display.set_mode((900, 900))
background_colour = (255, 255, 255)
engine = pyttsx3.init()
display_surface = pygame.display.set_mode((900, 900 ))

pngs = [x for x in glob("animals\\*.PNG")]
names = [x.split(".")[0] for x in glob("animals\\*.PNG")]
goodjob = pygame.image.load('animals/lion.png')
white = (255, 255, 255)
display_surface.fill(white)

animals = {k:v for k, v in zip(pngs, names)}
print(animals)

print(pngs)
print(names)

for n, animals in enumerate(pngs):
    display_surface.blit(goodjob, (0, 0))
    guess_counter = 0
    carImg = pygame.image.load(os.path.join('', animals))
    gameDisplay.blit(carImg,(0,0))
    pygame.display.update()
    for j in range(1,4):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                engine.say('Spell The Word')
                engine.runAndWait()
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print(text)
                except:
                    print('Did not get that try Again')
                    text=''
                if text == names[n].split("\\")[1]:
                    engine.say('good job')
                    display_surface.blit(goodjob, (0, 0))
                    engine.runAndWait()
                    break
                else:
                    if guess_counter < 3:
                        print('wrong try again')
                        guess_counter += 1
                    else:
                        print("\nSorry no more chances\n\n")
    time.sleep(2)


pygame.quit()