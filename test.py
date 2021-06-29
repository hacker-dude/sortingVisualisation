import pygame
import numpy
import time
import sys
from constants import *

x = numpy.random.randint(low=LOWER_LIMIT, high=UPPER_LIMIT, size=SIZE)

# print(x)  # temp
n = SIZE
theme = DARK
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
display.fill(theme)


def draw(arr, index):
    for i, num in enumerate(arr):
        if i == index or i == index + 1:  # temp
            pygame.draw.rect(display, BLUE, (50 + 9 * i, 600 - num * 3 - 30, 5, num * 3))  # temp
        else:  # temp
            pygame.draw.rect(display, (num + 150, 20, 60), (50 + 9 * i, 600 - num * 3 - 30, 5, num * 3))  # temp
        # pygame.draw.rect(display, RED, (20 + 15 * i, 600 - num * 3 - 30, 10, num * 3))


sorting = 0


def sortit():
    # for i in range(n):
    for j in range(n - sorting - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
        display.fill(theme)
        draw(x, j)
        pygame.display.flip()


clock = pygame.time.Clock()  # temp
draw(x, 10000)  # temp
pygame.display.flip()  # temp
time.sleep(1)  # temp

while True:
    # clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print(x)
            sys.exit()
    if sorting != n:
        sortit()
        sorting += 1
        # time.sleep(0.005)
    else:
        draw(x, 100000)
        pygame.display.flip()
        display.fill(theme)

# print(x)


# currently the main file
