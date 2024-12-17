import RPi.GPIO as GPIO
import time
import sys
import signal
 
def configurer():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(DEL_PIN, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(BTN_PIN,GPIO.IN,pull_up_down = GPIO.PUD_UP)       # Configuration bouton d'armement en entrée
  GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, bouncetime=250) 
 
def terminer(signum, frame):
  print("Fin du test")
  GPIO.output(DEL_PIN, GPIO.LOW)
  GPIO.cleanup()
  sys.exit(0)
 
DEL_PIN = 18
BTN_PIN = 17
 
def main():
  while True:
    if GPIO.input(BTN_PIN):
        GPIO.output(DEL_PIN, GPIO.LOW)
        print("Bouton relaché")
        time.sleep(1)
    else:
        GPIO.output(DEL_PIN, GPIO.HIGH)
        print("Bouton pressé")
        time.sleep(1)
 
if __name__ == '__main__':
  print("Test BTN_PIN")
  configurer()
  signal.signal(signal.SIGINT, terminer) # Pour terminer proprement
  main()