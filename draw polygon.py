import pygame
from pygame.locals import *

pygame.init()

GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

width = 640
length = 320
screen = pygame.display.set_mode((width, length))

background = GRAY

running = True
drawing = False
points = []

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            drawing = False
        elif event.type == MOUSEMOTION and drawing is True:
            points[-1] = event.pos
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                points.pop()

    screen.fill(background)
    if len(points) > 1:
        rect = pygame.draw.lines(screen, RED, True, points, 3)
        pygame.draw.rect(screen, BLUE, rect, 1)

    pygame.display.update()

pygame.quit()
