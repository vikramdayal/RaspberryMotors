#!/usr/bin/env python3

# Name: example_timer_servo.py
# Author: Vikram Dayal

# Advanced example of how to use the servos interface with timing waits.
# As shown in the simple examples, the setAngleAndWait call creates a
# sequencing problem, especially when we have a larger number of servo
# motors to control at the same time. Ideally, we would like to trigger all
# servos together and then wait for them to respond in one shot. Keep in mind that
# not all servos will respond in the same time. The servos package takes care of these
# multiple timing issues and comes out after the slowest of the servos times out.

# In this example, we are connecting two servo control
# to GPIO pin 11,13 (RasberryPi 4 and 3 are good with it)

#import the servos package from motors module
from motors import servos

def main():
    print("starting example")

    #create the servo objects , connected to GPIO board pin #11 and 13
    s1 = servos.servo(pin=11, waitTime=0.5)
    s2 = servos.servo(pin=13, waitTime=1.0)

    #operate the servos. Note, we are using setAngle function
    #which signals the servo but does not wait, so we will explicitly wait
    s1.setAngle(0)   # move S1 to default position of zero degrees
    s2.setAngle(0)   # move S2 to default position of zero degrees
    #now wait for the  both servos to respond. In this example it will wait
    # for max(0.5, 1.0)= 1.0 seconds
    servos.wait()

    s1.setAngle(180) # move S1 position of 180 degrees
    s2.setAngle(180) # move S2 position of 180 degrees
    #now wait for the  both servos to respond. In this example it will wait
    # for max(0.5, 1.0)= 1.0 seconds
    servos.servo.wait()

    s1.setAngle(0)   # move S1 back to position of zero degrees
    servos.wait() # it will wait for 0.5 seconds because there waitime for s1 is 0.5

    s2.setAngle(0)   # move S2 back to position of zero degrees
    servos.wait() # it will wait for 1 second because there waitime for s2 is 1.0

    # we are done with the servo pin shut them down
    s1.shutdown();
    s2.shutdown();


if __name__ == "__main__":
    main()