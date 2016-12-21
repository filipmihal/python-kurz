 import RPi.GPIO as GPIO, time, os      
 
DEBUG = 1
GPIO.setmode(GPIO.BOARD)
 
def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(1.5)
 
        GPIO.setup(RCpin, GPIO.IN)
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
 
while True:                                     
        if RCtime(12) <  6000:
	    print ("Je svetlo!")
	elif RCtime(12) <  9000:
	    print ("Je pritmie")
	else:
	    print ("Je tma!")  
