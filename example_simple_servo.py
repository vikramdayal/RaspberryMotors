#!/usr/bin/env python3

# Name: example_simple_servo.py
# Author: Vikram Dayal
# simple example of how to use the servos interface.
# In this example, we are connecting a sinle servo control
# to GPIO pin 11 (RasberryPi 4 and 3 are good with it)

#import the servos package from motors module
from motors import servos

def main():
    print("starting example")

    #create a servo object, connected to GPIO board pin #11
    s1 = servos.servo(11)

    #operate the servos. Note, we are using setAngleAndWait function
    #which waits for a specific time (default 1 sec) for the servo to react
    s1.setAngleAndWait(0)   # move to default position of zero degrees
    s1.setAngleAndWait(180) # move to position of 180 degrees

    #in the above examples, the servo will wait for default 1 second to respond, we
    #can change the respond time in seconds, in this example, we will wait 0.5 seconds
    s1.setAngleAndWait(0, 0.5)   # move back to position of zero degrees

    # we are done with the servo pin shut it down
    s1.shutdown();


if __name__ == "__main__":
    main()