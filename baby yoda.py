import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Baby Yoda')

YODAGREEN = (118, 158,157)
yodaImg = pygame.image.load("Baby_yoda.png")
yodaImg = pygame.transform.scale(yodaImg, (100, 80))
yodaX = 10
yodaY = 10

#Game loop
while True:
    screen.fill(YODAGREEN)

    screen.blit(yodaImg, (yodaX, yodaY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
