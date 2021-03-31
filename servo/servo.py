import RPi.GPIO as GPIO
from time import sleep

class servo:
    """ servo class first create the servo class with port
        number. Then test it to figure out the 180 degree rotation """

    mode=GPIO.BOARD
    servoCount=0
    active=[None]*40 #there are 40 GPIO pins in a Rasberry Pi


    #static method
    def setMode(self,newMode):
        print("Setting mode ", newMode, " Old mode", servo.mode)
        GPIO.setmode(newMode)
        servo.mode=newMode


    def __init__(self,port,min=2.0,max=10.5,waitTime=0.5):
      self.port = port
      self.min = min
      self.max = max
      self.last = 0
      self.waitTime=waitTime
      if servo.servoCount == 0:
          self.setMode(servo.mode)
      GPIO.setup(port, GPIO.OUT)
      self.pwm=GPIO.PWM(port, 50)
      self.pwm.start(0)
      servo.servoCount = servo.servoCount + 1
      servo.active[port]=self  #register the io port for other activities


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
        # cleaned. For reuse of the same port, it is important to actually del
        # pwm and let GC do it's business
        del self.pwm
        if servo.servoCount == 0:
            GPIO.cleanup()
            print("closed last port shutdown happened")


    def getDuty(self,degs):
        duty = 0.005556 *(self.max - self.min) * float(degs) + self.min
        print("duty=",duty)
        return duty


    #SetAngleAndWait
    # this function is the simple implementation when there a few servos in play and
    # one can wait for the servo to respond
    def setAngleAndWait(self,degs):
        duty=self.getDuty(degs)
        self.pwm.ChangeDutyCycle(duty)
        # wait for servo to respond and then set duty cycle to zero
        sleep(self.waitTime)
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
        servo.active[self.port]=self


    def waittime(p):
        if p is None:
            return 0
        return p.waitTime

    #wait
    #sleeps for max wait time of the servos called by setAngle and then and then
    # changes duty cycle to zero
    def wait():
        t=max(servo.active, key=servo.waittime)
        print("Waiting for ", t)
        sleep(t.waitTime)
        #cycle through active and change duty to zero
        cnt=0
        for s in servo.active:
            if s is not None:
                s.pwm.ChangeDutyCycle(0)
            servo.active[cnt]=None
        print("done reset duty")