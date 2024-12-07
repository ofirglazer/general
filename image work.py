import pygame
from pygame.locals import *


pygame.init()
GRAY = (127, 127, 127)
width = 640
height = 320
screen = pygame.display.set_mode((width, height))
RED = (255, 0, 0)


img = pygame.image.load('bird.png')
img = img.convert_alpha()
img_rect = img.get_rect()

background = GRAY

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    img_rect.center = (width // 2, height // 2)

    screen.fill(background)
    screen.blit(img, img_rect)
    pygame.draw.rect(screen, RED, img_rect, 1)
    pygame.display.update()

pygame.quit()