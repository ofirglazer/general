import pygame
from pygame.locals import *


pygame.init()
GRAY = (127, 127, 127)
width = 640
height = 320
screen = pygame.display.set_mode((width, height))
RED = (255, 0, 0)


img0 = pygame.image.load('bird.png')
img0 = img0.convert_alpha()
x = width // 2
y = height // 2
background = GRAY

running = True
moving = False
angle = 0
scale = 1

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if img_rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving is True:
            x += event.rel[0]
            y += event.rel[1]
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                angle += 10
            elif event.key == K_LEFT:
                angle -= 10
            elif event.key == K_UP:
                scale *= 1.1
            elif event.key == K_DOWN:
                scale /= 1.1

    img = pygame.transform.rotozoom(img0, angle, scale)
    img_rect = img.get_rect()
    img_rect.move_ip(x, y)


    screen.fill(background)
    screen.blit(img, img_rect)
    pygame.draw.rect(screen, RED, img_rect, 1)
    pygame.display.update()

pygame.quit()