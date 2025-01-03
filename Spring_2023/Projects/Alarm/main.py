import RPi.GPIO as GPIO
import time
import sys
import signal
import smtplib

class Email:
    SMTP_USER = "sejbouchereau@gmail.com"
    SMTP_PASSWORD = "xxx"
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    emailFrom: str
    nameFrom: str
    emailTo: str
    nameTo: str

    def __init__(self, emailFrom, nameFrom, emailTo, nameTo):
        self.emailFrom = emailFrom
        self.nameFrom = nameFrom
        self.emailTo = emailTo
        self.nameTo = nameTo

    def send(self, objet, msg):
        entete = ("From: "+ self.nameFrom +" <" + self.emailFrom + ">\n"
            "To: " + self.nameFrom + " <" + self.emailTo + ">\n"
            "Subject:" + objet + "\n\n")
        print(entete + msg)
        try:
            server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
            server.ehlo()
            server.login(self.SMTP_USER, self.SMTP_PASSWORD)
            server.sendmail(self.emailFrom, self.emailTo, (entete + msg))
            server.close()
        except smtplib.SMTPException:
            print("Impossible d'envoyer le mail a " + self.emailTo)
        except (smtplib.socket.error, smtplib.SMTPConnectError):
            print("Connexion impossible au serveur SMTP")

def configurer():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DEL_PIN, GPIO.OUT, initial=GPIO.LOW)              # Configuration DEL d'armement en sortie
    GPIO.setup(ALARM_PIN, GPIO.OUT, initial=GPIO.LOW)            # Configuration DEL alarme en sortie
    GPIO.setup(BTN_PIN,GPIO.IN,pull_up_down = GPIO.PUD_UP)       # Configuration bouton d'armement en entrée
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, bouncetime=250) 
    GPIO.setup(CONTACT_PIN,GPIO.IN,pull_up_down = GPIO.PUD_UP)   # Configuration contact magnétique entrée
    GPIO.add_event_detect(CONTACT_PIN, GPIO.FALLING, bouncetime=50)
    
    # Dans le cas présent où le capteur magnétique est remplacé par un fil, le
    # bouncetime a été ajusté pour mieux correspondre au temps nécessaire pour
    # modifier l'état du capteur.

def terminer(signum, frame):   # Fonction pour terminer proprement
    print("Exécution terminée")
    GPIO.cleanup()
    sys.exit(0)
    
BTN_PIN = 17       # Initialisation bouton d'armement
DEL_PIN = 18       # Initialisation de la DEL d'armement
ALARM_PIN = 23     # Initialisation DEL alarme
CONTACT_PIN = 22   # Initialisation contact magnétique

def alarm():       # Fonction appellée lorsque l'alarme est activée
    while True:
        if GPIO.input(ALARM_PIN):            # On fait clignoter la DEL
            GPIO.output(ALARM_PIN, GPIO.LOW)
            time.sleep(0.5)
        elif GPIO.event_detected(BTN_PIN):   # Condition de désactivation de l'alarme: On vérifie l'état du bouton d'armement
            GPIO.output(ALARM_PIN, GPIO.LOW) # On éteint la DEL d'alarme
            GPIO.output(DEL_PIN, GPIO.LOW)   # On éteint la DEL d'armement
            print("Alarme désactivée")
            break                            # On sort de la fonction alarm()
        else:
            GPIO.output(ALARM_PIN, GPIO.HIGH)
            time.sleep(0.5)
        
def main():   # Programme principal
    while True:
        if GPIO.event_detected(BTN_PIN):         # On vérifie un changement d'état du bouton d'armement
            if GPIO.input(DEL_PIN):              # Condition de désactivation du système: on vérifie si la DEL d'armement est allumée
                GPIO.output(DEL_PIN, GPIO.LOW)   # la DEL d'armement s'éteint
                print("Système inactif")
                time.sleep(0.5)
            else:
                print("Système actif ✔️")         # Condition d'activation du système
                GPIO.output(DEL_PIN, GPIO.HIGH)  # La DEL d'armement s'allume
                time.sleep(0.5)
        elif GPIO.event_detected(CONTACT_PIN):   # Condition d'activation de l'alarme: On attend un changement d'état du capteur magnétique
            if GPIO.input(DEL_PIN):              # On regarde si le système est actif
                GPIO.output(DEL_PIN, GPIO.LOW)   # Éteint la DEL d'armement du système
                print("Intrusion détectée: Alarme activée")
                email = Email("sejbouchereau@gmail.com", "Samuel B",
                              "sejbouchereau@gmail.com", "Samuel B")
                email.send("Alarme déclenchée", "Alarme")  # Envoie un courriel
                alarm()                          # Appel la fonction alarm()

if __name__ == '__main__':
    print("Samuel Bouchereau - Projet 1:")
    print("simulation d'un système d'alarme")
    configurer()
    signal.signal(signal.SIGINT, terminer)
    main()
