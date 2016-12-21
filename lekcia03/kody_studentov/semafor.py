import RPi.GPIO as GPIO
import time
#nastavim mod cislovania pinov
GPIO.setmode(GPIO.BOARD)
#vypnem upozornenia od GPIO
GPIO.setwarnings(False)
#nastavim si piny, ktore idem pouzivat. GPIO.OUT  znamena, ze dany pin nebude citat data ale poslielat energiu
#zelena
GPIO.setup(40,GPIO.OUT)
#zlta
GPIO.setup(33,GPIO.OUT)
#cervena
GPIO.setup(29,GPIO.OUT)

#funkcia, ktora na sekundu zasvieti
def zasviet(pin, doba):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(doba)
    GPIO.output(pin,GPIO.LOW)
while True:
	zasviet(40,4)
	zasviet(33,0.5)
	zasviet(29,5)
	zasviet(33,0.5)
GPIO.cleanup()
