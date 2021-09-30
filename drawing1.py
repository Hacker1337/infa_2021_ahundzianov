import math

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (50, 255, 255)
white = (255, 255, 255)
grey = (230, 230, 230)


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
def elips(*coords, color=grey):
    # Вводить нужно координаты, а не ширину и высоту
    a = ellipse(screen, color, (coords[0], coords[1], coords[2]-coords[0], coords[3]-coords[1]))
    b = ellipse(screen, black, (coords[0], coords[1], coords[2]-coords[0], coords[3]-coords[1]), width=1)


rect(screen, white, (0, 600, 1500, 600))
rect(screen, blue, (0, 0, 1500, 600))

# медведь
elips(140, 430, 310, 525)
elips(2, 490, 260, 950)
lines(screen, black, False, [(264, 695), (317, 600), (633, 338)], width=7)  # удочка
elips(215, 590, 330, 635)
elips(150, 820, 330, 950)
elips(260, 930, 400, 974)
elips(145, 425, 177, 452)
elips(208, 447, 219, 459, color=black)
elips(298, 447, 308, 459, color=black)

elips(443, 780, 754, 871, color=(77, 77, 77))   # серая фигня в лунке
elips(480, 810, 715, 871, color=(20, 80, 68))   # зеленая
line(screen, black, (633, 338), (633, 830))     # леска
lines(screen, black, False, [(200, 499), (277, 497), (309, 485)])     # улыбка
# a = ellipse(screen, white, (10, 600, 300, 600))
# b = ellipse(screen, black, (10, 600, 300, 600), width=1)
# pygame.transform.rotate(screen, 45)
fishy = (190, 200, 200)

rect(screen, fishy, [(544, 950), (150, 36)])
rect(screen, black, [(544, 950), (150, 36)], width=1)
polygon(screen, fishy, [(544, 950+18), (544-36, 950), (544-36, 950+36)])
polygon(screen, black, [(544, 950+18), (544-36, 950), (544-36, 950+36)], width=1)
circle(screen, (121, 121, 242), (544+150-25, 950+18), 10)
polygon(screen, (221, 166, 166), [(620, 949), (620, 950-30), (620+40, 949)])


def light(angle):
    cent = (515, 191)
    color = (249, 255, 191)
    r = 200
    width = 0.3
    polygon(screen, color, [cent, (cent[0] + r*math.sin(angle), cent[1] + r*math.cos(angle)), (cent[0] + r*math.sin(angle+width), cent[1] + r*math.cos(angle+width))])

for a in [0.63*i for i in range(10)]:
    light(a)
circle(screen, (217, 221, 12), (515, 191), 50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
