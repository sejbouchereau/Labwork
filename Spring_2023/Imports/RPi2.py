import RPi.GPIO as GPIO
import time

BTN_PIN = 17
DEL_PIN = 18

print("Bouton et DEL")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DEL_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(BTN_PIN, GPIO.IN,
           pull_up_down=GPIO.PUD_UP)  #set up a falling detect on ButtonPin,and callback function to ButtonLed
GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, bouncetime=500)

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
