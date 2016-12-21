import RPi.GPIO as GPIO
import time
#nastavim mod cislovania pinov
GPIO.setmode(GPIO.BOARD)
#vypnem upozornenia od GPIO
GPIO.setwarnings(False)
#nastavim si piny, ktore idem pouzivat. GPIO.OUT  znamena, ze dany pin nebude citat data ale poslielat energiu
GPIO.setup(13,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

GPIO.cleanup()
