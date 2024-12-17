import RPi.GPIO as GPIO
import time
import sys
import signal
 
def configurer():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(DEL_PIN, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(CONTACT_PIN,GPIO.IN,pull_up_down = GPIO.PUD_UP)       # Configuration bouton d'armement en entrée
  GPIO.add_event_detect(CONTACT_PIN, GPIO.FALLING, bouncetime=250) 
 
def terminer(signum, frame):
  print("Fin du test")
  GPIO.output(DEL_PIN, GPIO.LOW)
  GPIO.cleanup()
  sys.exit(0)
 
DEL_PIN = 18
CONTACT_PIN = 22
 
def main():
  while True:
    if GPIO.input(CONTACT_PIN):
        GPIO.output(DEL_PIN, GPIO.LOW)
        print("Contact rompu")
        time.sleep(1)
    else:
        GPIO.output(DEL_PIN, GPIO.HIGH)
        print("Contact établi")
        time.sleep(1)
 
if __name__ == '__main__':
  print("Test CONTACT_PIN")
  configurer()
  signal.signal(signal.SIGINT, terminer) # Pour terminer proprement
  main()