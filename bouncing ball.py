import pygame
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

width = 1024
length = 780
screen = pygame.display.set_mode((width, length))

running = True
background = GRAY

ball = pygame.image.load("ball.png")
rect = ball.get_rect()
speed = [1, 1]

while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
            # if event.key == pygame.K_r:
            #     background = RED
            # elif event.key == pygame.K_g:
            #     background = GREEN

    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > length:
        speed[1] = -speed[1]


    screen.fill(background)
    pygame.draw.rect(screen, WHITE, rect, 1)
    screen.blit(ball, rect)
    pygame.display.set_caption(f"background color is {background}")
    pygame.display.update()

pygame.quit()
