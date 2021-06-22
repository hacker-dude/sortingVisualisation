import pygame
import numpy
import time
import sys

x = numpy.random.randint(low=1, high=100, size=50)
# print(x)
n = 50
pygame.init()
display = pygame.display.set_mode((1000, 600))


def draw(arr):
    for i, num in enumerate(arr):
        # if i == ind or i == ind + 1:
        #     pygame.draw.rect(display, (42, 183, 202), (10 + 9.5 * i, 600-num*3-30, 1000/n - 5, num*3))
        # else:
        pygame.draw.rect(display, (220, 20, 60), (10 + 10 * i, 600 - num * 3 - 30, 5, num * 3))


sorting = 0


def sortit():
    # for i in range(n):
    for j in range(n - sorting - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]


clock = pygame.time.Clock()
while True:
    # clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print(x)
            sys.exit()
    if sorting != n:
        sortit()
        sorting += 1
        time.sleep(0.05)

    draw(x)
    pygame.display.flip()
    display.fill((244, 244, 248))

# print(x)
