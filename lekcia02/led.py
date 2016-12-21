import RPi.GPIO as GPIO 
import time as t
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11, GPIO.OUT) 
GPIO.output(11,True) 
t.sleep(15)
GPIO.output(11,False)
GPIO.cleanup()
