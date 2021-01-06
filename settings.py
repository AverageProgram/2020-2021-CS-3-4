import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 300
PLAYER_IMG = 'default(3).png'

#wall settings
WALL_IMG = 'wall2.png'

#text function
font_name = pygame.font.match_font('arial')
def draw_tex(surf,text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface =font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.miptop = (x, y)
    surf.blit(text_surface, text_rect)
