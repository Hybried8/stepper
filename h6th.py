import RPi.GPIO as GPIO
import time
import lcd_i2c
import numpy

inputstring1 = "Finished. Enjoy" #The string we send to the first line of the LCD
inputstring2 = ""#The string we send to the second line of the LCD

try:
    lcd_i2c.printer(inputstring1, inputstring2) #prints to LCD
    time.sleep(5)#sleep for 5 seconds

except KeyboardInterrupt: #stops try if (ctrl + c) is pressed
    pass
    

GPIO.cleanup()
lcd_i2c.cleanup()