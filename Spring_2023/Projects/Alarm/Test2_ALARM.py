import RPi.GPIO as GPIO
import time
import sys
import signal
 
def configurer():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(ALARM_PIN, GPIO.OUT, initial=GPIO.LOW)
 
def terminer(signum, frame):
  print("Fin du test")
  GPIO.output(ALARM_PIN, GPIO.LOW)
  GPIO.cleanup()
  sys.exit(0)
 
ALARM_PIN = 23
 
def main():
  while True:
      if GPIO.input(ALARM_PIN):
          GPIO.output(ALARM_PIN, GPIO.LOW)
          print("DEL Off")
          time.sleep(2)
      else:
          GPIO.output(ALARM_PIN, GPIO.HIGH)
          print("DEL On")
          time.sleep(2)
 
if __name__ == '__main__':
  print("Test ALARM_PIN")
  configurer()
  signal.signal(signal.SIGINT, terminer) # Pour terminer proprement
  main()