#nacitanie kniznic as = ako ju budeme volat
import RPi.GPIO as GPIO
import time

#nie az tak podstatne veci 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
#nastavi pin 13 
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
#vypne pin 
GPIO.output(13, 0)
GPIO.output(11, 0)
#zapne
GPIO.output(13, 1)
GPIO.output(11, 1)
time.sleep(5)
#vypne
GPIO.output(11, 0)
GPIO.output(13, 0)
GPIO.cleanup()
