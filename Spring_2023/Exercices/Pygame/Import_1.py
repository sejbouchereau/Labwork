import pygame
import math


class objBouton:
    def __init__(self, couleur, x, y, rayon, texte=''):
        self.couleur = couleur
        self.x = x
        self.y = y
        self.rayon = rayon
        self.texte = texte

    def dessiner(self, screen):
        sysfont = pygame.font.get_default_font()
        font = pygame.font.SysFont(None, 36)
        pygame.draw.circle(screen, self.couleur, (self.x, self.y), self.rayon)
        txtBtn = font.render(self.texte, True, (0, 0, 0))
        rectBtn = txtBtn.get_rect()
        rectBtn.center = (self.x, self.y)
        screen.blit(txtBtn, rectBtn)

    def isOverBouton(self, posSouris):
        xSouris = posSouris[0]
        ySouris = posSouris[1]

        absX = (self.x - xSouris) ** 2
        absY = (self.y - ySouris) ** 2

        return (math.sqrt(absX + absY) < self.rayon)


if __name__ == "__main__":
    print("Début du test")
    pygame.init()

    GRIS = (200, 200, 200)
    BLANC = (255, 255, 255)

    screen = pygame.display.set_mode([500, 500])

    btn = objBouton(GRIS, 250, 150, 75, "ON")
    btn2 = objBouton(GRIS, 250, 350, 75, "OFF")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                xSouris, ySouris = pygame.mouse.get_pos()
                if btn.isOverBouton((xSouris, ySouris)):
                    print("Clic bouton!")

        screen.fill(BLANC)

        btn.dessiner(screen)
        btn2.dessiner(screen)

        pygame.display.flip()

    pygame.quit()
    print("Fin du test")
