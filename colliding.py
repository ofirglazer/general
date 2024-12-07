import pygame
from pygame.locals import *
import random

pygame.init()

GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# YELLOW = (255, 255, 0)

width = 640
height = 320


def random_point():
    x = random.randrange(width)
    y = random.randrange(height)
    return x, y


def randon_points(n_points):
    points = []
    for point in range(n_points):
        points.append(random_point())
    return points


def randon_rects(n_rects):
    rects = []
    for point in randon_points(n_rects):
        rects.append(Rect(point, (20, 20)))
    return rects

screen = pygame.display.set_mode((width, height))

background = GRAY

running = True
moving = False
rect = Rect(50, 60, 200, 80)
direction_dict = {K_UP: (0, -5), K_DOWN: (0, 5), K_LEFT: (-5, 0), K_RIGHT: (5, 0)}

n_points = 100
n_rects = 50
points = randon_points(n_points)
rects = randon_rects(n_rects)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_r:
                points = randon_points(n_points)
                rects = randon_rects(n_rects)

    screen.fill(background)
    pygame.draw.rect(screen, RED, rect, 2)
    for point in points:
        if rect.collidepoint(point):
            pygame.draw.circle(screen, GREEN, point, 4, 0)
        else:
            pygame.draw.circle(screen, BLACK, point, 4, 0)
    for rand_rect in rects:
        if rect.colliderect(rand_rect):
            pygame.draw.rect(screen, GREEN, rand_rect, 2, 0)
        else:
            pygame.draw.rect(screen, BLACK, rand_rect, 2, 0)


    pygame.display.flip()

pygame.quit()
