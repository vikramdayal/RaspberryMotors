#!/usr/bin/env python3

'''
 The servos package. It supports the supports the servo class and the following functions:



# Name: __main__.py
# Author: Vikram Dayal
'''

import RPi.GPIO as GPIO
from time import sleep

######################################################################
# service functions provided by servos package. They are a short
# cut to servos.servo.xxx static functions
######################################################################

def setMode(mode):
    '''
    set the GPIO mode to define the pins. To be called before doing anything with GPIO

    usage examples:
        servos.setMode(RPi.GPIO.BOARD) # default
        servos.setMode(GPIO.BCM) # refer to the pins by the "Broadcom SOC channel" number

    '''
    servo.setMode(mode)


def wait(tw=None):
    '''
    Wait for the minimum of wt and maximum waitTime of all devices that are currently
    performing setAngle operations. If no argument is provided then wait for the maximum
    of waitTime of all servos performing the setAngle operations.

    Usage example 1:
        servos.wait()
    Expected behavior:
         if the servo waitTimes are [0.5, 0.8], it will wait for 0.8 seconds

    Usage example 2:
        servos.wait(wt)
    Expected behavior:
         if the servo waitTimes are [0.5, 0.8] and wt=0.25, it will wait for 0.25 seconds
         if the servo waitTimes are [0.5, 0.8] and wt=0.75, it will wait for 0.75 seconds
         if the servo waitTimes are [0.5, 0.8] and wt=0.9,  it will wait for 0.8 seconds


    '''
    servo.wait(tw)


def calibrate(pin,duty):
    '''
    Calibrate function that takes a pin number and duty. It sets the duty cycle
    of the device to allow for measure of the angle that corresponds to the
    duty cycle.

    Instructions on how to use the function:
    1. Wire up the servo motor as per instructions (let us say we wired up on GPIO pin 11,
       rest of instructions are for pin 11)
    2. From the home directory of this project, run the following command:
         python3 -m RaspberryMotors.motor --pin=11 --duty=2.0

    Observe the motor position. Vary the value of duty cycle in the above command till you
    observe the stepper motor is at position zero. Note that the motor will not rotate any
    further if you keep decreasing the value of duty cycle. Take the highest value of duty
    cycle when the angle is still zero.

    Repeat the same steps in increasing values to get the corresponding value of duty cycle
    closest to 180 degrees. In the python code, instantiate the servo object as
    per the following code:
         s1 = servos.servo(pin=11, min=2.0,max=10.5,waitTime=0.5)

    '''

    s1 = servo(pin)
    s1.testDuty(duty)
    s1.shutdown()


def ResetGpioAtShutdown(flag):
    '''
    By default when the last servo is shutdown, the GPIO is cleaned up for safety. However,
    this might not be the desireable effect if GPIO is being used for other purposes. In such
    cases, at the outset of the script, issue the following:
       ResetGpioAtShutdown(False)

    '''
    servo.ResetGpioAtShutdown(flag)

class servo:
    """
    Encapuslates all operations that are required for servo opartations

    Example code:
    s1 = servos.servo(pin=11, waitTime=0.5)
    s2 = servos.servo(pin=13, waitTime=1.0)

    """

    mode=GPIO.BOARD
    servoCount=0
    active=[None]*40 #there are 40 GPIO pins in a Rasberry Pi
    resetGpioAtShutdownFlag=True


    #static method
    def setMode(newMode):
        '''
        set the GPIO mode to define the pins. Service function, should not be called
        directly from the code. Use the servo.setMode(mode) instead.

        '''
        print("Setting mode ", newMode, " Old mode", servo.mode)
        GPIO.setmode(newMode)
        servo.mode=newMode


    def ResetGpioAtShutdown(flag):
        '''
        Sets the GPIO cleanup flag. Service function, should not be called
        directly from the code. Use the servo.ResetGpioAtShutdown(flag) instead.

        '''
        servo.resetGpioAtShutdownFlag=flag
        print("resetGpioAtShutdownFlag set to ", servo.resetGpioAtShutdownFlag)


    def __init__(self,pin,min=2.0,max=10.5,waitTime=1.0):
        '''
        Constructor of the servo class. Only pin number is required.
        min and max correspond to the duty cycle values corresponding to 0 degrees and
        180 degrees. If these values are not specified, the system assumes defaultof 2.0
        and 10.5 respectively.

        If waitTime is not specified, then a default of 1 second is assumed.

        '''

        self.pin = pin
        self.min = min
        self.max = max
        self.last = 0
        self.waitTime=waitTime
        print("waitTime=", waitTime)
        if servo.servoCount == 0:
          servo.setMode(servo.mode)
        GPIO.setup(pin, GPIO.OUT)
        self.pwm=GPIO.PWM(pin, 50)
        self.pwm.start(0)
        servo.servoCount = servo.servoCount + 1


    #duty is tested: start with 2 for zero degrees and 10.5 for 180
    def testDuty(self,duty):
        '''
        Directly test out the servo by changing the duty cycle. This
        function is used for calibaration purposes only.
        '''
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)
        self.pwm.ChangeDutyCycle(0)

    def shutdown(self):
        '''
        Issue a pwm.stop() to clean up the pwm that has been setup.

        if resetGpioAtShutdownFlag has not been set to False, when the last
        servo shutdown() is called, a GPIO.cleanup() is perfomed.

        Note:
        It appears that the internal pointers to the pwm structures are not getting
        cleaned. For reuse of the same pin, so we actaully del pwm to let GC do it's
        business.
     '''
        self.pwm.stop()
        servo.servoCount = servo.servoCount - 1

        # note about following code:
        # looks like the internal pointers to the pwm structures are not getting
        # cleaned. For reuse of the same pin, it is important to actually del
        # pwm and let GC do it's business
        del self.pwm
        if servo.servoCount == 0 and servo.resetGpioAtShutdownFlag:
            GPIO.cleanup()
            print("closed last pin shutdown happened")


    def getDuty(self,degs):
        duty = 0.005556 *(self.max - self.min) * float(degs) + self.min
        print("duty=",duty)
        return duty


    def setAngleAndWait(self,degs,t=None):
        '''
        This function is the simple implementation when there a few servos in play and
        one can wait for the servo to respond
        '''
        duty=self.getDuty(degs)
        self.pwm.ChangeDutyCycle(duty)

        if t is None:
            t = self.waitTime
        # wait for servo to respond and then set duty cycle to zero
        sleep(t)
        self.pwm.ChangeDutyCycle(0)



    # SetAngle
    def setAngle(self,degs):
        '''
        This function is the simple implementation when there a several servos in play or
        one cannot wait for each servo to respond. Typical usage would be:
           s1.setAngle(10)
           s2.setAngle(100)
           servo.wait()
        '''
        duty=self.getDuty(degs)
        self.pwm.ChangeDutyCycle(duty)
        servo.active[self.pin]=self


    def waittime(p):
        if p is None:
            return 0
        return p.waitTime

    #wait
    #sleeps for max wait time of the servos called by setAngle and then and then
    # changes duty cycle to zero
    def wait(wt=None):
        '''
        Waits for max wait time of the servos called by setAngle and then and then
        changes duty cycle to zero. Service function, should not be called
        directly from the code. Use the servo.wait(flag) instead.
        '''
        t=max(servo.active, key=servo.waittime)
        w=t.waitTime
        if wt is not None:
            w=min(w, wt)
        print("Waiting for ", w)
        sleep(w)
        #cycle through active and change duty to zero
        cnt=0
        for s in servo.active:
            if s is not None:
                s.pwm.ChangeDutyCycle(0)
            servo.active[cnt]=None
            cnt = cnt + 1
        print("done reset duty")