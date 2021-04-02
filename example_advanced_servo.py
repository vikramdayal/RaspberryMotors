#!/usr/bin/env python3

# Name: example_advanced_servo.py
# Author: Vikram Dayal
# Advanced example of how to use the servos interface.
# In this example, we are connecting a sinle servo control
# to GPIO pin 11 (RaspberryPi 4 and 3 are good with it)
# 1. We will connect using the BCM interface
#     refer: https://www.raspberrypi-spy.co.uk/2012/09/checking-your-raspberry-pi-board-version/
# 2. We will set ResetGpioAtShutdown(False), so GPIO auto cleanup will not be done on servo shutdown,
#    hence we will have do that inside our code.

# Wiring diagram
#   servo-1 (referred to S1 in the example code)
#   ---------------------------------------------
#   | servo wire | connected to GPIO pin on Pi  |
#   |------------|------------------------------|
#   | Brown      | 6 (GND)                      |
#   | Red        | 2 (5v power)                 |
#   | Yellow     | 11(GPIO 17 on Pi-4)          |
#   ---------------------------------------------

##############################################################
#import the servos package from motors module
from RaspberryMotors.motors import servos
import RPi.GPIO as GPIO

def main():
    print("starting example")

    servos.ResetGpioAtShutdown(False) # do not reset GPIO at last servo shutdown

    servos.setMode(GPIO.BCM) # refer to the pins by the "Broadcom SOC channel" number

    #create a servo object, connected to GPIO board pin #11 which stands for BCM GPIO pin 17
    # refer to https://www.raspberrypi-spy.co.uk/2012/09/checking-your-raspberry-pi-board-version/
    s1 = servos.servo(17)

    #operate the servos. Note, we are using setAngleAndWait function
    #which waits for a specific time (default 1 sec) for the servo to react
    s1.setAngleAndWait(0)   # move to default position of zero degrees
    s1.setAngleAndWait(180) # move to position of 180 degrees

    #in the above examples, the servo will wait for default 1 second to respond, we
    #can change the respond time in seconds, in this example, we will wait 0.5 seconds
    s1.setAngleAndWait(0, 0.5)   # move back to position of zero degrees

    # we are done with the servo pin shut it down
    s1.shutdown();

    #since GPIO cleanup is not done automatically, we have to do it within our code here
    GPIO.cleanup()


if __name__ == "__main__":
    main()