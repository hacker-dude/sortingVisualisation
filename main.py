import sys

import pygame
import pygame as pg
import time
import numpy as np

n = 51


def generate():
    return np.random.randint(low=1, high=100, size=n)


def draw(arr, ind):
    for i, num in enumerate(arr):
        if i == ind or i == ind + 1:
            pg.draw.rect(display, (num+100, 20, 60), (20 + 15 * i, 600-num*3-30, 10, num*3))
        else:
            pg.draw.rect(display, (num+100, 20, 60), (20 + 15 * i, 600-num*3-30, 10, num*3))


def sort():
    for i in range(n):
        for j in range(0, n - i - 1):
            draw(x, j)
            pg.display.update()
            time.sleep(0.005)
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
            display.fill((244, 244, 248))
    # while True:
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             print(x)
    #             pygame.quit()
    #             sys.exit()
    #     draw(x, 10000)
    #     pg.display.update()
       # pg.



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
# time.sleep(3)
sort()
