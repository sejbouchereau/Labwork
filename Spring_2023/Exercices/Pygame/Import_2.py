import pygame
from pygame.locals import *

ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((250, 250))
rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(100, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    point = pygame.mouse.get_pos()

    if rect.collidepoint(point):
        couleur = BLANC
    else:
        couleur = ROUGE

    screen.fill(NOIR)
    pygame.draw.rect(screen, couleur, rect)
    pygame.display.flip()

pygame.quit()
