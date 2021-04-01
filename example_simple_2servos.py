# Name: example_simple_2servos.py
# Author: Vikram Dayal
# simple example of how to use the servos interface.
# In this example, we are connecting two servo control
# to GPIO port 11,13 (RasberryPi 4 and 3 are good with it)

#import the servos package from motors module
from motors import servos

def main():
    print("starting example")

    #create the servo objects , connected to GPIO board port #11 and 13
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

    # we are done with the servo ports shut them down
    s1.shutdown();
    s2.shutdown();


if __name__ == "__main__":
    main()