import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(29,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

c=int(input("Zadaj cas vybuchu bomby: "))
GPIO.output(29,GPIO.LOW)
#funkcia, ktora na sekundu zasvieti
def zasviet(pin, doba):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(doba)
    GPIO.output(pin,GPIO.LOW)

for i in range(0,c):
	print(c)
	c=c-1
	zasviet(29,2)
	time.sleep(2)
