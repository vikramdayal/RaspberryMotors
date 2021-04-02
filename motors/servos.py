#!/usr/bin/env python3


# Name: __main__.py
# Author: Vikram Dayal
# The servos package. It supports the supports the servo class and the following functions:
#
# setMode(mode) : set the GPIO mode to define the pins. To be called before doing anything
#                 with GPIO
# usage examples:
#    servos.setMode(RPi.GPIO.BOARD)

# wait(): Wait for the max waitime of all devices that are currently performing setAngle
#         operations
# usage examples:
#    servos.wait()


# wait(wt): Wait for the min wt and max waitTime of all devices that are currently performing setAngle
#         operations.
# usage examples:
#    servos.wait(wt)
# For example:
#     if servo waitTimes are [0.5, 0.8] and wt=0.25, it will wait for 0.25 seconds
#     if servo waitTimes are [0.5, 0.8] and wt=0.75, it will wait for 0.75 seconds
#     if servo waitTimes are [0.5, 0.8] and wt=0.9,  it will wait for 0.8 seconds


# calibrate(pin,duty): calibrate function that takes a pin number and duty. It sets the duty cycle
#                      of the device to allow for measure of the angle that corresponds to the
#                      duty cycle


# ResetGpioAtShutdown(flag): By default when the last servo is shutdown, the GPIO is cleaned up for safety
#                            However, this might not be the desireable effect if GPIO is being used for
#                            other purposes. In such cases, at the outset of the script, issue the following:
#                                ResetGpioAtShutdown(False)
#

import RPi.GPIO as GPIO
from time import sleep

######################################################################
# service functions provided by servos package. They are a short
# cut to servos.servo.xxx static functions
######################################################################

def setMode(mode):
    servo.setMode(mode)


def wait(tw=None):
    servo.wait(tw)


def calibrate(pin,duty):
    s1 = servo(pin)
    s1.testDuty(duty)
    s1.shutdown()


def ResetGpioAtShutdown(flag):
    servo.ResetGpioAtShutdown(flag)

########################################################################
# class servo, which encapuslates all operations that are required for
# servo opartations
########################################################################
class servo:
    """ servo class first create the servo class with pin
        number. Then test it to figure out the 180 degree rotation """

    mode=GPIO.BOARD
    servoCount=0
    active=[None]*40 #there are 40 GPIO pins in a Rasberry Pi
    resetGpioAtShutdownFlag=True


    #static method
    def setMode(newMode):
        print("Setting mode ", newMode, " Old mode", servo.mode)
        GPIO.setmode(newMode)
        servo.mode=newMode


    def ResetGpioAtShutdown(flag):
        servo.resetGpioAtShutdownFlag=flag
        print("resetGpioAtShutdownFlag set to ", servo.resetGpioAtShutdownFlag)


    def __init__(self,pin,min=2.0,max=10.5,waitTime=1.0):
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
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)
        self.pwm.ChangeDutyCycle(0)

    def shutdown(self):
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


    #SetAngleAndWait
    # this function is the simple implementation when there a few servos in play and
    # one can wait for the servo to respond
    def setAngleAndWait(self,degs,t=None):
        duty=self.getDuty(degs)
        self.pwm.ChangeDutyCycle(duty)

        if t is None:
            t = self.waitTime
        # wait for servo to respond and then set duty cycle to zero
        sleep(t)
        self.pwm.ChangeDutyCycle(0)



    # SetAngle
    # this function is the simple implementation when there a several servos in play or
    # one cannot wait for each servo to respond. Typical usage would be:
    # s1.setAngle(10)
    # s2.setAngle(100)
    # servo.wait()
    def setAngle(self,degs):
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