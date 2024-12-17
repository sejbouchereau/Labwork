import RPi.GPIO as GPIO
import time
import sys
import signal


def configurer():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DEL_PIN, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, bouncetime=500)


def terminer(signum, frame):
    print("Terminer")
    GPIO.cleanup()
    sys.exit(0)


BTN_PIN = 17
DEL_PIN = 18


def main():
    while True:
        if GPIO.event_detected(BTN_PIN):
            print("Bouton pressé")
            if GPIO.input(DEL_PIN):
                GPIO.output(DEL_PIN, GPIO.LOW)
                print("DEL On")
            else:
                GPIO.output(DEL_PIN, GPIO.HIGH)
                print("DEL Off")
            time.sleep(0.5)


if __name__ == '__main__':
    print("Bouton et DEL")
    configurer()
    signal.signal(signal.SIGINT, terminer)  # Pour terminer proprement
    main()
