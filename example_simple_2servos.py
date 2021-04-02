#!/usr/bin/env python3

# Name: example_simple_2servos.py
# Author: Vikram Dayal
# simple example of how to use the servos interface.
# In this example, we are connecting two servo control
# to GPIO pin 11,13 (RaspberryPi 4 and 3 are good with it)

# Wiring diagram
#   servo-1 (referred to S1 in the example code)
#   ---------------------------------------------
#   | servo wire | connected to GPIO pin on Pi  |
#   |------------|------------------------------|
#   | Brown      | 6 (GND)                      |
#   | Red        | 2 (5v power)                 |
#   | Yellow     | 11(GPIO 17 on Pi-4)          |
#   ---------------------------------------------
#   servo-2 (referred to S2 in the example code)
#   ---------------------------------------------
#   | servo wire | connected to GPIO pin on Pi  |
#   |------------|------------------------------|
#   | Brown      | 14(GND)                      |
#   | Red        | 4 (5v power)                 |
#   | Yellow     | 13(GPIO 27 on Pi-4)          |
#   ---------------------------------------------

##############################################################
#import the servos package from motors module
from motors import servos

def main():
    print("starting example")

    #create the servo objects , connected to GPIO board pin #11 and 13
    s1 = servos.servo(11)
    s2 = servos.servo(13)

    #operate the servos. Note, we are using setAngleAndWait function
    #which waits for a specific time (default 1 sec) for the servo to react
    s1.setAngleAndWait(0)   # move S1 to default position of zero degrees
    s2.setAngleAndWait(0)   # move S2 to default position of zero degrees
    s1.setAngleAndWait(180) # move S1 position of 180 degrees
    s2.setAngleAndWait(180) # move S2 position of 180 degrees

    #in the above examples, the servos will wait for default 1 second each to respond, we
    #can change the respond time in seconds, in this example, we will wait 0.5 seconds instead
    s1.setAngleAndWait(0, 0.5)   # move S1 back to position of zero degrees
    s2.setAngleAndWait(0, 0.5)   # move S2 back to position of zero degrees

    # we are done with the servo pin shut them down
    s1.shutdown();
    s2.shutdown();


if __name__ == "__main__":
    main()