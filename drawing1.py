import math

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1200))

# Useful colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (50, 255, 255)
white = (255, 255, 255)
grey = (230, 230, 230)
fishy = (190, 200, 200)


def elips(*coords, color=grey):
    """
    Drawing ellipsis by its coords instead of w and h
    :param coords: position of the figure
    :param color: is actually a color
    :return: None
    """
    ellipse(screen, color, (coords[0], coords[1], coords[2] - coords[0], coords[3] - coords[1]))
    ellipse(screen, black, (coords[0], coords[1], coords[2] - coords[0], coords[3] - coords[1]), width=1)


def draw_rod(coords=(0, 0), scale=1.):
    """
    Drawing fishing rod
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    x0, y0 = coords
    lines(screen, black, False, [((264 - 2) * scale + x0, 275 * scale + y0), ((317 - 2) * scale + x0, 180 * scale + y0),
                                 ((633 - 2) * scale + x0, -78 * scale + y0)], width=7)
    line(screen, black, ((633 - 2) * scale + x0, (338 - 430) * scale + y0),
         ((633 - 2) * scale + x0, (830 - 430) * scale + y0))


def draw_body(coords=(0, 0), scale=1.):
    """
    Drawing bear's body
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    x0, y0 = coords
    elips((140 - 2) * scale + x0, (430 - 420) * scale + y0, 308 * scale + x0,
          105 * scale + y0)
    elips((2 - 2) * scale + x0, (490 - 420) * scale + y0, 258 * scale + x0, 530 * scale + y0)
    elips((215 - 2) * scale + x0, (590 - 420) * scale + y0, 328 * scale + x0,
          215 * scale + y0)
    elips((150 - 2) * scale + x0, (820 - 420) * scale + y0, 328 * scale + x0,
          530 * scale + y0)
    elips((260 - 2) * scale + x0, (930 - 420) * scale + y0, 398 * scale + x0,
          554 * scale + y0)
    elips((145 - 2) * scale + x0, (425 - 420) * scale + y0, 175 * scale + x0,
          32 * scale + y0)
    elips((208 - 2) * scale + x0, (447 - 420) * scale + y0, 217 * scale + x0,
          39 * scale + y0, color=black)
    elips((298 - 2) * scale + x0, (447 - 420) * scale + y0, 306 * scale + x0,
          39 * scale + y0, color=black)
    lines(screen, black, False, [((200 - 2) * scale + x0, (499 - 430) * scale + y0),
                                 ((277 - 2) * scale + x0, (497 - 430) * scale + y0),
                                 ((309 - 2) * scale + x0, (485 - 430) * scale + y0)])


def draw_bear(coords=(0, 0), scale=1.):
    """
    Drawing the BEAR
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    x0, y0 = coords
    x0 += 2
    y0 += 420
    draw_rod(coords=(x0, y0), scale=scale)
    draw_body(coords=(x0, y0), scale=scale)


def draw_lake(coords=(0, 0), scale=1.):
    """
    Drawing the lake
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    x0, y0 = coords
    x0 += 2
    y0 += 420
    elips((443 - 2) * scale + x0, (780 - 420) * scale + y0, 752 * scale + x0,
          451 * scale + y0, color=(77, 77, 77))  # серая фигня в лунке
    elips((480 - 2) * scale + x0, (810 - 420) * scale + y0, 713 * scale + x0,
          451 * scale + y0, color=(20, 80, 68))  # зеленая


def draw_fish(coords=(0, 0), scale=1.):
    """
    Drawing the fish
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    size = (150 * scale, 36 * scale)
    x, y = coords
    x = (x + 544) * scale
    y = (y + 950) * scale
    rect(screen, fishy, ((x, y), size))
    rect(screen, black, ((x, y), size), width=1)
    polygon(screen, fishy, [(x, y + size[1] // 2), (x - size[1], y), (x - size[1], y + size[1])])
    polygon(screen, black, [(x, y + size[1] // 2), (x - size[1], y), (x - size[1], y + size[1])], width=1)
    circle(screen, (121, 121, 242), (x + size[0] - size[1] * 3 // 4, y + size[1] // 2), 10 * scale)
    polygon(screen, (221, 166, 166),
            [(x + size[0] // 2 + 1, y - 1), (x + size[0] // 2 + 1, y - 30), (x + size[0] // 2 + 1 + 40, y - 1)])


def draw_sun(coords=(0, 0), scale=1.0, n=10):
    """
    Drawing the sun
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :param n: Num of rays
    :return: None
    """
    x, y = coords
    x += 515
    y += 191
    for a in [2 * math.pi / n * i for i in range(n)]:
        light(a, cent=coords, scale=scale)
    circle(screen, (217, 221, 12), (x, y), 50 * scale)


def light(angle, cent=(0, 0), scale=1.):
    """
    Drawing one ray.
    :param angle: that is angle
    :param cent: coords of the center
    :param scale: resize of the object
    :return:
    """
    x0, y0 = cent
    x0 += 515
    y0 += 191
    color = (249, 255, 191)
    r = 200 * scale
    width = 0.3 * scale
    polygon(screen, color, [(x0, y0), (x0 + r * math.sin(angle), y0 + r * math.cos(angle)),
                            (x0 + r * math.sin(angle + width), y0 + r * math.cos(angle + width))])


def draw_bg(scale=1.):
    """
    Drawing of the background
    :param scale: resize param
    :return: None
    """
    h = 600 * scale
    rect(screen, white, (0, h, 800, 1200 - h))
    rect(screen, blue, (0, 0, 800, h))


def end():
    """
    End of drawing
    :return: None
    """
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


def draw_pic(coords=(0, 0), scale=1.):
    """
    Drawing the picture
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    draw_bg(scale=scale)
    draw_lake(coords=coords, scale=scale)
    draw_bear(coords=coords, scale=scale)
    draw_fish(coords=coords, scale=scale)
    draw_sun(coords=coords, scale=scale)
    end()


draw_pic(scale=.75)
