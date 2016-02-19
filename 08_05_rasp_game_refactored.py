#08_05_rasp_game_refactored.py

import pygame
from pygame.locals import *

import random

from sys import exit


score = 0

screen_width = 600
screen_height  = 400

spoon_x = 300
spoon_y = screen_height - 50

class Raspberry:
    x = 0
    y = 0

    def __init__(self):
        self.x = random.randint(10, screen_width)
        self.y = 0

    def update(self):
        self.y += 5
        if self.y > spoon_y -15:
            self.y = 0
            self.x = random.randint(10, screen_width)
        self.x += random.randint(-5, 5)

        if self.x < 10:
            self.x = 10
        if self.x > screen_width - 20:
            self.x = screen_width - 20
        screen.blit(raspberry_image, (self.x, self.y))

    def is_caught(self):
        return self.y >= spoon_y -15 and self.x >= spoon_x -30 and \
               self.x < spoon_x +20

clock = pygame.time.Clock()
r = Raspberry()

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Raspberry Catching')

spoon = pygame.image.load('spoon.jpg').convert()
raspberry_image = pygame.image.load('raspberry.jpg').convert()




    
def update_spoon():
    global spoon_x
    global spoon_y
    spoon_x, ignore = pygame.mouse.get_pos()
    screen.blit(spoon, (spoon_x, spoon_y))

def display(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, 1, (10,10,10))
    screen.blit(text, (0,0))
    
def check_for_catch():
    global score
    if r.is_caught():
        score +=1
    
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255,255,255))
    r.update()
    update_spoon()
    check_for_catch()
    display("Score: " + str(score))
    pygame.display.update()
    clock.tick(30)


