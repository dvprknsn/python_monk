#08_03_rasp_game_one.py

import pygame
import random
from pygame.locals import *
from sys import exit
screen_width = 600
score = 0
spoon_x = 300
spoon_y = 300
raspberry_x = 300
raspberry_y = 0

pygame.init()

screen = pygame.display.set_mode((screen_width, 400))
pygame.display.set_caption('Raspberry Catching')

spoon = pygame.image.load('spoon.jpg').convert()

raspberry = pygame.image.load('raspberry.jpg').convert()


def update_spoon():
    global spoon_x
    global spoon_y
    spoon_x, ignore = pygame.mouse.get_pos()
    screen.blit(spoon, (spoon_x, spoon_y))

def update_raspberry():
    global raspberry_x
    global raspberry_y
    raspberry_y +=5
    if raspberry_y > spoon_y:
        raspberry_y = 0
        raspberry_x = random.randint(10, screen_width)
    raspberry_x += random.randint(-5,5)
    if raspberry_x < 10:
        raspberry_x = 10
    if raspberry_x > screen_width - 20:
        raspberry_x = screen_width - 20
    screen.blit(raspberry, (raspberry_x, raspberry_y))

def display(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, 1, (10,10,10))
    screen.blit(text, (0,0))
    

def check_for_catch():
    global score
    if raspberry_y >= spoon_y -1 and raspberry_x >= spoon_x -30  and \
       raspberry_x < spoon_x + 20:
        score +=1
    display("Score: " + str(score))

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255,255,255))
    update_spoon()
    update_raspberry()
    check_for_catch()

    pygame.display.update()
    clock.tick(30)


