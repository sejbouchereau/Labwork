'''
Fichier : config/Config.py
'''
import logging

class Config():
    def __init__(self):
        # Niveau des logs
        self.LOG_LEVEL = logging.DEBUG
        #self.LOG_LEVEL = logging.CRITICAL

        # E-mail
        self.EMAIL_USER = "xxx.yyyl@CollegeAhuntsic.qc.ca"

        # Réglages de l'horloge
        self.wakeup = '8:30'
        self.close = '20:30'
        self.period = '00:00:05'

        # Chemin du répertoire des albums
        self.path = '/home/pi/Documents/Albums/'
        
        # Délai
        self.delay = 5

