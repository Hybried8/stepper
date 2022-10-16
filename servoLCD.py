import RPi.GPIO as GPIO
import lcd_i2c
import time
import numpy

#General GPIO Pin Setup
GPIO.setmode(GPIO.BCM)
servoPIN = 18 #selects the pin for the servo motor
GPIO.setup(servoPIN, GPIO.OUT) #set the servoPIN to an output

lcd_i2c.lcd_init()

#PWM Pin Setup
p = GPIO.PWM(servoPIN, 50) # GPIO 18 is set for PWM with 50Hz
p.start(2.5) # Initialization of the PWM pin and duty cycle

#use of try/except to get out of loop when needed (ctrl + c)
try:
    lcd_i2c.printer("Servo will now","begin")
    while True: #starts main loop
        time.sleep(1) #sleeps for 1 second at start of loop each time, a good idea in repeated loops to ensure LCD is readable between stages
        lcd_i2c.printer("Going","Counterclockwise")
        for dutyCycle in numpy.arange (2.5,12,0.25): #gives evenly spaced non-integer values within the range
            p.ChangeDutyCycle(dutyCycle) #changes duty cycle incremently to rotate the servo
            time.sleep(0.025) #timestep between each change in dutycycle
        time.sleep(1)
        lcd_i2c.printer("Going","Clockwise")
        for dutyCycle in numpy.arange (12,2.5,-0.25):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(0.025)

except KeyboardInterrupt:
    # Cleanup after (ctrl + c) is pressed
    print("Cleaning up!") #tells the user cleanup is occuring
    p.stop() #stops PWM pin
    lcd_i2c.cleanup() #cleansup the LCD
    GPIO.cleanup() #cleansup GPIO pins used in the script"""