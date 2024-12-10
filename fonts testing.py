import pygame

pygame.init()

RED = (255, 0, 0)
GRAY = (127, 127, 127)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

background = GRAY

# fonts = pygame.font.get_fonts()
# print(len(fonts))
# for f in fonts:
#     print(f)

print(f"system font is {pygame.font.get_default_font()}")

width = 640
height = 320
screen = pygame.display.set_mode((width, height))

font1 = pygame.font.SysFont("arial", 48)
font2 = pygame.font.SysFont("narkisim", 56)
font3 = pygame.font.SysFont("freesansbold", 72)

img1 = font1.render("arial", True, RED)
img2 = font2.render("םיסיקרנ", True, YELLOW)
img3 = font3.render("freesansbold", True, CYAN)
rect = img1.get_rect()

pygame.draw.rect(img1, BLUE, rect, 1)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)
    screen.blit(img1, (20, 20))
    screen.blit(img2, (20, 80))
    screen.blit(img3, (20, 120))

    pygame.display.flip()

pygame.quit()