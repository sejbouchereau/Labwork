import RPi.GPIO as GPIO
import time
import sys
import signal


def configurer():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DEL_PIN, GPIO.OUT, initial=GPIO.LOW)


def terminer(signum, frame):
    print("Terminer")
    GPIO.output(DEL_PIN, GPIO.LOW)
    GPIO.cleanup()
    sys.exit(0)


DEL_PIN = 17


def main():
    while True:
        if GPIO.input(DEL_PIN):
            GPIO.output(DEL_PIN, GPIO.LOW)
            print("DEL Off")
        else:
            GPIO.output(DEL_PIN, GPIO.HIGH)
            print("DEL On")
        time.sleep(0.5)


if __name__ == '__main__':
    print("DEL Blink")
    configurer()
    signal.signal(signal.SIGINT, terminer)  # Pour terminer proprement
    main()
