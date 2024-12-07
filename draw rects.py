import pygame
from pygame.locals import *

pygame.init()

GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


width = 640
length = 320
screen = pygame.display.set_mode((width, length))

background = GRAY

running = True
drawing = False
rect_start = (0, 0)
rect_size = (0, 0)
rects = []
points_in_rect = ('topleft', 'topright', 'bottomleft', 'bottomright',
'midtop', 'midright', 'midbottom', 'midleft', 'center')
font = pygame.font.Font(None, 24)


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            rect_start = event.pos
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            rect_end = event.pos
            rect_size = (rect_end[0] - rect_start[0], rect_end[1] - rect_start[1])
            drawing = False
            rect = pygame.Rect(rect_start, rect_size)
            print(f"x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}, left={rect.left}, top={rect.top},"
                  f"right={rect.right}, bottom={rect.bottom}, center={rect.center}")
            rects.append(rect)
            rect_start = (0, 0)
            rect_size = (0, 0)
        elif event.type == MOUSEMOTION and drawing == True:
            rect_end = event.pos
            rect_size = (rect_end[0] - rect_start[0], rect_end[1] - rect_start[1])

    screen.fill(background)
    for rect in rects:
        pygame.draw.rect(screen, RED, rect, 3)
        for point in points_in_rect:
            pos = eval('rect.' + point)
            img = font.render(point, True, BLACK)
            screen.blit(img, pos)
            pygame.draw.circle(screen, GREEN, pos, 5)


    pygame.draw.rect(screen, BLUE, (rect_start, rect_size), 1)

    # pygame.draw.rect(screen, RED, (50, 20, 12, 100))
    # pygame.draw.rect(screen, BLUE, (150, 100, 120, 100))
    # pygame.draw.rect(screen, GREEN, (100, 60, 120, 200))
    # pygame.draw.rect(screen, RED, (350, 20, 120, 100), 1)
    # pygame.draw.rect(screen, GREEN, (400, 60, 120, 100), 4)
    # pygame.draw.rect(screen, BLUE, (450, 100, 120, 100), 8)

    # pygame.draw.ellipse(screen, RED, (50, 20, 100, 100))
    # pygame.draw.ellipse(screen, GREEN, (100, 60, 130, 100))
    # pygame.draw.ellipse(screen, BLUE, (150, 100, 160, 100))
    # pygame.draw.ellipse(screen, RED, (350, 20, 160, 100), 1)
    # pygame.draw.ellipse(screen, GREEN, (400, 60, 160, 100), 4)
    # pygame.draw.ellipse(screen, BLUE, (450, 100, 160, 100), 8)

    pygame.display.update()


pygame.quit()