import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1500, 1500))

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (50, 255, 255)
white = (255, 255, 255)

'''
rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)
'''

rect(screen, white, (0, 900, 1500, 600))
rect(screen, blue, (0, 0, 1500, 900))


a = ellipse(screen, white, (10, 600, 300, 600))
b = ellipse(screen, black, (10, 600, 300, 600), width=1)
pygame.transform.rotate(screen, 45)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
