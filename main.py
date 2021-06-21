import sys

import pygame
import pygame as pg
import time
import numpy as np


n = 50


def generate():
    return np.random.randint(low=1, high=100, size=n)


def draw(arr, ind):
    for i, num in enumerate(arr):
        if i == ind or i == ind + 1:
            pg.draw.rect(display, 'blue', (20+ 15 * i, 0, 10, num))
        else:
            pg.draw.rect(display, 'red', (20+ 15 * i, 0, 10, num))


def sort():
    for i in range(n):
        for j in range(0, n - i - 1):
            draw(x, j)
            pg.display.update()
            time.sleep(0.005)
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
            display.fill(('white'))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pygame.quit()
                sys.exit()



running = True
pg.init()
display = pg.display.set_mode((800, 600))
x = generate()
#
# while running:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             running = False
#     pg.display.flip()
#     #for i in range(10):
#         #time.sleep(.5)
#         #  pg.draw.rect(display, 'red', (300, 400, 10, i*10))
#
#     #print(x)
#     pg.display.update()
time.sleep(3)
sort()
draw()