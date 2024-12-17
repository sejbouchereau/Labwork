import random
import signal
import sys
import time

import RPi.GPIO as GPIO


def configurer():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RED_PIN, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(BLUE_PIN, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, bouncetime=500)


def terminer(signum, frame):
    print("Terminer")
    GPIO.cleanup()
    sys.exit(0)


BTN_PIN = 17
RED_PIN = 23
BLUE_PIN = 18


def main():
    while True:
        delay = random.uniform(0.2, 0.8)  # génération d'un délai aléatoire entre 0.2 et 0.8 secondes
        GPIO.output(RED_PIN, GPIO.LOW)  # allume la DEL rouge
        GPIO.output(BLUE_PIN, GPIO.HIGH)  # éteint la DEL bleue
        time.sleep(delay)  # attends le délai aléatoire
        GPIO.output(RED_PIN, GPIO.HIGH)  # éteint la DEL rouge
        GPIO.output(BLUE_PIN, GPIO.LOW)  # allume la DEL bleue
        time.sleep(delay)  # attends le délai aléatoire


if __name__ == '__main__':
    print("Bouton et DEL")
    configurer()
    signal.signal(signal.SIGINT, terminer)  # Pour terminer proprement
    main()
