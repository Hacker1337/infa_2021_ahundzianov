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



def draw_bear(x0, y0, xsize=630, ysize=510):     # медведь
    """x0, y0 - top left corner"""
    Ysize = 510     # default size
    Xsize = 630     # default size
    lines(screen, black, False, [((264-2)*xsize//Xsize+x0, 695), ((317-2)*xsize//Xsize+x0, 600), ((633-2)*xsize//Xsize+x0, 338)], width=7)  # удочка
    elips((140-2)*xsize//Xsize+x0, (430-420)*ysize//Ysize+y0, 310*xsize//Xsize, 525*ysize//Ysize)
    elips((2-2  )*xsize//Xsize+x0, (490-420)*ysize//Ysize+y0, 260*xsize//Xsize, 950*ysize//Ysize)
    elips((215-2)*xsize//Xsize+x0, (590-420)*ysize//Ysize+y0, 330*xsize//Xsize, 635*ysize//Ysize)
    elips((150-2)*xsize//Xsize+x0, (820-420)*ysize//Ysize+y0, 330*xsize//Xsize, 950*ysize//Ysize)
    elips((260-2)*xsize//Xsize+x0, (930-420)*ysize//Ysize+y0, 400*xsize//Xsize, 974*ysize//Ysize)
    elips((145-2)*xsize//Xsize+x0, (425-420)*ysize//Ysize+y0, 177*xsize//Xsize, 452*ysize//Ysize)
    elips((208-2)*xsize//Xsize+x0, (447-420)*ysize//Ysize+y0, 219*xsize//Xsize, 459*ysize//Ysize, color=black)
    elips((298-2)*xsize//Xsize+x0, (447-420)*ysize//Ysize+y0, 308*xsize//Xsize, 459*ysize//Ysize, color=black)

    elips((443-2)*xsize//Xsize+x0, (780-420)*ysize//Ysize+y0, 754*xsize//Xsize, 871*ysize//Ysize, color=(77, 77, 77))  # серая фигня в лунке
    elips((480-2)*xsize//Xsize+x0, (810-420)*ysize//Ysize+y0, 715*xsize//Xsize, 871*ysize//Ysize, color=(20, 80, 68))  # зеленая
    line(screen, black, ((633-2)*xsize//Xsize+x0, (338-430)*ysize//Ysize+y0), ((633-2)*xsize//Xsize+x0, (830-430)*ysize//Ysize+y0))  # леска
    lines(screen, black, False, [((200-2)*xsize//Xsize+x0, (499-430)*ysize//Ysize+y0), ((277-2)*xsize//Xsize+x0, (497-430)*ysize//Ysize+y0), ((309-2)*xsize//Xsize+x0, (485-430)*ysize//Ysize+y0)])  # улыбка


draw_bear(2, 420)


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
