import speech_recognition as sr
import time
from glob import glob
import pygame
import os
import pyttsx3
import random

pygame.init()

gameDisplay = pygame.display.set_mode((900, 900))
background_colour = (255, 255, 255)
engine = pyttsx3.init()


pngs = [x for x in glob("animals\\*.PNG")]
pic = random.sample(pngs, k=5)



names = [x.split(".")[0] for x in glob("animals\\*.PNG")]
white = (255, 255, 255)


animals = {k:v for k, v in zip(pic, names)}
# print(animals)

# print(pic)
print(pic)
# print(names)

for n, animals in enumerate(pic):
    guess_counter = 0
    carImg =pygame.image.load(os.path.join('', animals))
    gameDisplay.fill((white))
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
                    engine.runAndWait()
                    break
                elif text == 'quit':
                        pygame.quit()
                else:
                    if guess_counter < 3:
                        print('wrong try again')
                        guess_counter += 1
                    else:
                        print("\nSorry no more chances\n\n")
    time.sleep(1)


pygame.quit()