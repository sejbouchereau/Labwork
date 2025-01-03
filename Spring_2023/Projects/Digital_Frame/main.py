## Samuel Bouchereau - Projet 3: Câdre intelligent ##

import RPi.GPIO as GPIO                                          # Importation des bibliothèques
from config import *
import os
import time
import pygame
from pygame.locals import *

pygame.init()                                                    # Initialisation de la bibliothèque pygame

class Main(Config):
    def __init__(self):
        super().__init__()                                       # Initialisation des attributs de configuration
        BTN1_PIN = 17                                            # Numéro de la broche GPIO pour le bouton 1
        BTN2_PIN = 18                                            # Numéro de la broche GPIO pour le bouton 2
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BTN1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)        # Configuration de la broche BTN1_PIN en entrée avec résistance de pull-up
        GPIO.add_event_detect(BTN1_PIN, GPIO.FALLING, bouncetime=300)  # Détection d'interruption sur le bouton 1
        GPIO.setup(BTN2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)        # Configuration de la broche BTN2_PIN en entrée avec résistance de pull-up
        GPIO.add_event_detect(BTN2_PIN, GPIO.FALLING, bouncetime=300)  # Détection d'interruption sur le bouton 2
        pygame.mouse.set_visible(False)                                # Masquer le curseur de la souris

    def afficher_image(self, image_path):                   # Affiche une image en plein écran avec pygame
        screen = pygame.display.set_mode([1152, 864])       # Création de la fenêtre d'affichage avec une résolution spécifique
        largeur, hauteur = pygame.display.Info().current_w, pygame.display.Info().current_h     # Récupération de la résolution de l'écran
        fenetre = pygame.display.set_mode((largeur, hauteur), pygame.FULLSCREEN)                # Création de la fenêtre en plein écran
        image = pygame.image.load(image_path)                       # Chargement de l'image à partir du chemin spécifié
        image = pygame.transform.scale(image, (largeur, hauteur))   # Redimensionnement de l'image pour qu'elle corresponde à la résolution de l'écran
        fenetre.blit(image, (0, 0))                         # Afficher l'image dans la fenêtre
        pygame.display.flip()                               # Rafraîchissement de l'affichage
        time.sleep(self.delay)

    def album1(self):
        print("Album_1")
        album = "Album_1"                                   # Nom de l'album sélectionné (1er par défaut)
        photos_directory = os.path.join(self.path, album)   # Chemin vers le répertoire contenant les photos de l'album
        photo_files = [file for file in os.listdir(photos_directory) if file.lower().endswith(('.jpg', '.png'))]
        
        # Ne récupère les fichiers photos que s'ils ne se terminent par ".jpg" ou ".png"

        BTN1_PIN = 17
        BTN2_PIN = 18
        while True:
            for photo_file in photo_files:
                if os.path.isfile(os.path.join(photos_directory, photo_file)):
                    print("Affichage de la photo :", photo_file)
                    image_path = os.path.join(photos_directory, photo_file)     # Chemin complet vers le fichier image
                    self.afficher_image(image_path)                             # Affichage de l'image
                    if GPIO.event_detected(BTN2_PIN):                           # Si le bouton 2 est pressé
                        self.mode_veille()                                      # Passage en mode veille
                    if GPIO.event_detected(BTN1_PIN):                           # Si le bouton 1 est pressé
                        self.album2()                                           # Passage à l'album suivant
                    time.sleep(self.delay)

    def album2(self):
        print("Album_2")
        album = "Album_2"
        photos_directory = os.path.join(self.path, album)
        photo_files = [file for file in os.listdir(photos_directory) if file.lower().endswith(('.jpg', '.png'))]

        BTN1_PIN = 17
        BTN2_PIN = 18
        while True:
            for photo_file in photo_files:
                if os.path.isfile(os.path.join(photos_directory, photo_file)):
                    print("Affichage de la photo :", photo_file)
                    image_path = os.path.join(photos_directory, photo_file)
                    self.afficher_image(image_path)                             # Affichage de l'image
                    if GPIO.event_detected(BTN2_PIN):                           # Si le bouton 2 est pressé
                        self.mode_veille()                                      # Passage en mode veille
                    if GPIO.event_detected(BTN1_PIN):                           # Si le bouton 1 est pressé
                        self.album3()                                           # Passage à l'album suivant
                    time.sleep(self.delay)

    def album3(self):
        print("Album_3")
        album = "Album_3"
        photos_directory = os.path.join(self.path, album)
        photo_files = [file for file in os.listdir(photos_directory) if file.lower().endswith(('.jpg', '.png'))]

        BTN1_PIN = 17
        BTN2_PIN = 18
        while True:
            for photo_file in photo_files:
                if os.path.isfile(os.path.join(photos_directory, photo_file)):
                    image_path = os.path.join(photos_directory, photo_file)
                    self.afficher_image(image_path)                             # Affichage de l'image
                    if GPIO.event_detected(BTN2_PIN):                           # Si le bouton 2 est pressé
                        self.mode_veille()
                    if GPIO.event_detected(BTN1_PIN):                           # Si le bouton 1 est pressé
                        self.album1()                                           # Retoune à l'album par défaut (1)
                    time.sleep(self.delay)

    def mode_veille(self):
        largeur, hauteur = pygame.display.Info().current_w, pygame.display.Info().current_h     # Récupération de la résolution de l'écran
        fenetre = pygame.display.set_mode((largeur, hauteur), pygame.FULLSCREEN)                # Création de la fenêtre du mode veille en plein écran
    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()                                   # Pour quitter le programme par l'affichage du mode veille
                    sys.exit(main)
                elif GPIO.event_detected(18):                       # Si le bouton 2 est pressé
                    self.album1()                                   # Débute le diaporama à l'album 1
            fenetre.fill((0, 0, 0))                                 # Remplissage de la fenêtre avec du noire
            pygame.display.flip()                                   # Rafraîchissement de l'affichage de la fenêtre
            if GPIO.event_detected(18):                             # Si le bouton 2 est pressé
                self.album1()                                       # Débute le diaporama à l'album 1  
            time.sleep(1)

def main(args):
    monProg = Main()
    monProg.mode_veille()                                           # Exécution de la méthode mode_veille
    return 0

if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.cleanup()
    import sys
    sys.exit(main(sys.argv))
