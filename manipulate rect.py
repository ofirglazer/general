import pygame
from pygame.locals import *

pygame.init()

GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)



width = 640
height = 320
screen = pygame.display.set_mode((width, height))

background = GRAY

running = True
rect0 = Rect(50, 60, 200, 80)
rect1 = Rect(100, 20, 100, 140)
direction_dict = {K_UP: (0, -5), K_DOWN: (0, 5), K_LEFT: (-5, 0), K_RIGHT: (5, 0)}


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_l:
                rect0.left = 0
            elif event.key == K_r:
                rect0.right = width
            elif event.key == K_c:
                rect0.centerx = width // 2
            elif event.key == K_t:
                rect0.top = 0
            elif event.key == K_b:
                rect0.bottom = height
            elif event.key == K_m:
                rect0.centery = height // 2
            elif event.key in direction_dict:
                if event.mod & pygame.KMOD_LSHIFT:
                    rect0.inflate_ip(direction_dict[event.key])
                else:
                    rect0.move_ip(direction_dict[event.key])

    screen.fill(background)
    union = rect0.union(rect1)
    clip = rect0.clip(rect1)
    pygame.draw.rect(screen, YELLOW, union)
    pygame.draw.rect(screen, GREEN, clip)
    pygame.draw.rect(screen, BLUE, rect0, 3)
    pygame.draw.rect(screen, RED, rect1, 3)

    pygame.display.flip()

pygame.quit()
