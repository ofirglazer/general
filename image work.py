import pygame
import math
from pygame.locals import *


pygame.init()
GRAY = (127, 127, 127)
width = 640
height = 320
screen = pygame.display.set_mode((width, height))
RED = (255, 0, 0)
MAGENTA = (255, 0, 255)


img0 = pygame.image.load('bird.png')
img0 = img0.convert_alpha()
angle = 0
scale = 1
mouse_start = mouse_current = (0, 0)

img = pygame.transform.rotozoom(img0, angle, scale)
x = width // 2
y = height // 2
background = GRAY

running = True
moving = False
scaling = False


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if img_rect.collidepoint(event.pos):
                moving = True
            else:
                scaling = True
                mouse_start = event.pos
        elif event.type == MOUSEBUTTONUP:
            moving = False
            scaling = False
        elif event.type == MOUSEMOTION and moving is True:
            x += event.rel[0]
            y += event.rel[1]
        elif event.type == MOUSEMOTION and scaling is True:
            mouse_current = event.pos
            dx = mouse_current[0] - mouse_start[0]
            dy = mouse_current[1] - mouse_start[1]
            d = math.sqrt(dx ** 2 + dy ** 2)
            angle = math.degrees(-math.atan2(dy, dx))
            scale = 5 * abs(d / width)
            img = pygame.transform.rotozoom(img0, angle, scale)

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                angle += 10
                img = pygame.transform.rotozoom(img0, angle, scale)
            elif event.key == K_LEFT:
                angle -= 10
                img = pygame.transform.rotozoom(img0, angle, scale)
            elif event.key == K_UP:
                scale *= 1.1
                img = pygame.transform.rotozoom(img0, angle, scale)
            elif event.key == K_DOWN:
                scale /= 1.1
                img = pygame.transform.rotozoom(img0, angle, scale)
            elif event.key == K_r:
                img = img0
                scale = 1
                angle = 0
                x = width // 2
                y = height // 2
            elif event.key == K_v:
                img = pygame.transform.flip(img, False, True)
            elif event.key == K_h:
                img = pygame.transform.flip(img, True, False)
            elif event.key == K_l:
                img = pygame.transform.laplacian(img)
            elif event.key == K_2:
                img = pygame.transform.scale2x(img)


    img_rect = img.get_rect()
    img_rect.center = (x, y)


    screen.fill(background)
    screen.blit(img, img_rect)
    pygame.draw.rect(screen, RED, img_rect, 1)
    pygame.draw.line(screen, MAGENTA, mouse_start, mouse_current, 1)
    pygame.draw.circle(screen, MAGENTA, mouse_start, 3)
    pygame.draw.circle(screen, MAGENTA, mouse_current, 3)
    pygame.display.update()

pygame.quit()