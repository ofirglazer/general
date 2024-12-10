import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


class App:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        App.width = 640
        App.height = 320
        App.flags = RESIZABLE
        App.screen = pygame.display.set_mode((App.width, App.height), App.flags)
        App.running = True
        App.text = Text("pygame App sample", (20, 20))
        App.shortcuts = {
            (K_x, KMOD_LALT): 'print("left alt + x")',
            (K_x, KMOD_LCTRL): 'print("left ctrl + x")',
            (K_f, KMOD_LALT): 'self.toggle_fullscreen()',
            (K_s, KMOD_LALT): 'self.toggle_resizeable()',
            (K_g, KMOD_LALT): 'self.toggle_frame()',
            (K_x, KMOD_LALT + KMOD_LSHIFT): 'print("left alt + left shift + x")'
        }

    def toggle_fullscreen(self):
        """"Toggle between full screen and windowed screen."""
        self.flags ^= FULLSCREEN
        self.screen = pygame.display.set_mode((0, 0), self.flags)

    def toggle_resizeable(self):
        """Toggle between resizable and fixed-size window."""
        self.flags ^= RESIZABLE
        self.screen = pygame.display.set_mode((App.width, App.height), self.flags)

    def toggle_frame(self):
        """"Toggle between frame and noframe window."""
        self.flags ^= NOFRAME
        self.screen = pygame.display.set_mode((App.width, App.height), self.flags)

    def do_shortcut(self, event):
        """Find the key/mod combination in the dictionary and execute the cmd."""
        key = event.key
        mod = event.mod
        if (key, mod) in App.shortcuts:
            exec(self.shortcuts[key, mod])

    def run(self):
        """Run the main event loop."""
        while App.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    App.running = False
                elif event.type == KEYDOWN:
                    self.do_shortcut(event)
                    # if event.key == K_s:
                    #    print("Key S pressed")

            App.screen.fill(GRAY)
            App.text.draw()
            pygame.display.flip()
        pygame.quit()


class Text:
    """"Create a text object."""

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        self.fontname = None
        self.fontsize = 72
        self.fontcolor = BLACK
        self.set_font()
        self.render_font()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render_font(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        App.screen.blit(self.img, self.pos)  # also working self.rect


class Scene:
    """Create a new scene (room, level, view)."""
    id = 0
    background  = GRAY

    def __init__(self, *args, **kwargs):
        # Append the new scene and make it the current scene
        App.scenes.append(self)
        App.scene = self

        # Set the instance id and increment the class id
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.background = Scene.background

    def draw(self):
        """Draw all objects in the scene."""
        App.screen.fill(self.background)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()

    def __str__(self):
        return f"Scene {self.id}"

if __name__ == '__main__':
    App().run()
