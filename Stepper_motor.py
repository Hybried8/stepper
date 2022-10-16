import RPi.GPIO as GPIO
import time
import lcd_i2c
import numpy

#Setup the RaspPi to use the numbering on the board
GPIO.setmode(GPIO.BCM)

controlPins = [21, 20, 12, 16]

# Setup the outputs Pins to control the stepper
GPIO.setup(controlPins[0], GPIO.OUT)
GPIO.setup(controlPins[1], GPIO.OUT)
GPIO.setup(controlPins[2], GPIO.OUT)
GPIO.setup(controlPins[3], GPIO.OUT)

# The following matrix should contain the coil energizing sequence for coils A, B, A', and B' 
halfstepSequence = [ [1,1,0,0],
                     [0,1,0,0],
                     [0,1,1,0],
                     [0,0,1,0],
                     [0,0,1,1],
                     [0,0,0,1],
                     [1,0,0,1],
                     [1,0,0,0],
                     ]

    #We will now go one full rotation - notice you can see the pins turn ON through the LEDs
for x in range (50): #Range is 50, as it needs 50 cycles through the halfstepSqeuence for a full rotation (each sequence loop represents a rotation of 7.2 degrees)
    for halfstep in range (len(halfstepSequence)): #Loop from 0 to len (length) of the half step sequence (8)
        for pin in range (len(controlPins)): #Loop from 0 to len (length) of controlPins (4)
            GPIO.output(controlPins[pin - 1], halfstepSequence[halfstep][pin - 1])
        time.sleep(0.05) #Adjustable for faster or slower speed (too fast and the stepper will stop working), if your connection is slow or you are debugging using the LEDs. Increase the value for slower response

    #We will now rotate back in the other direction
for x in range (50): #Range is 50, as it needs 50 cycles through the halfstepSqeuence for a full rotation (each sequence loop represents a rotation of 7.2 degrees)
    for halfstep in reversed (range (len(halfstepSequence))): #Loop from 0 to len (length) of the half step sequence (8)
        for pin in range (len(controlPins)): #Loop from 0 to len (length) of controlPins (4)
            GPIO.output(controlPins[pin - 1], halfstepSequence[halfstep][pin - 1])
        time.sleep(0.05) #Adjustable for faster or slower speed (too fast and the stepper will stop working), if your connection is slow or you are debugging using the LEDs. Increase the value for slower response.
        
GPIO.cleanup()