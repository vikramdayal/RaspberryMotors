# RasberryServo

Welcome to my Rasberry Pi service library. In this library I have started with an interface to control
sevro motors using the GPIO pins of the Rasberry pi. The driver for me to write the this library was that all
internet examples of using servos on Rasberry were too painful to set up PWM and claculate duty cycle! I wanted to 
control several servo motors simulatenously and was missing the quiet elegance on the Arduino Servo library.

If you want to figure out how to use my library, I would suggest
that you start by using the examples in the sequence provided below:

1. example_simple_servo.py: simple setup and control a single servo
2. example_simple_2servos.py: simple setup and control two servos sequentailly
3. example_timer_servo.py: advanced setup and control two servos simultaneously

By the time you are done with the third example, you should find that you can do pretty much anything with
Rasberry Pi and the Servo library.

Wiring required to run the example
==================================

The examples require two servo motors, I used Vilros SG90 (9g) and MicroServo DXW90 (9g) servos. Please feel free 
to use your own. Keep in mind if you are using the bigger servos you would have to power them sepearetly. The internet
is full of examples of how to wire up servos. In my example the wiring is very simple, to minimise power pins and segregate
power suppoy for the servos, feel free to use a breadboard instead.

Please note that by defualt, the library uses the GPIO.BOARD settings, which means that all pin numbers are defined as physical pin numbers. All examples assume physical pin numbers.

 servo-1 (refered to S1 in the example code)
 -------------------------------------------
 
    ---------------------------------------------
    | servo wire | connected to GPIO pin on Pi  |
    |------------|------------------------------|
    | Brown      | 6 (GND)                      |
    | Red        | 2 (5v power)                 |
    | Yellow     | 11(GPIO 17 on Pi-4)          |
    ---------------------------------------------


 servo-2 (refered to S2 in the example code)
 -------------------------------------------
 
    ---------------------------------------------
    | servo wire | connected to GPIO pin on Pi  |
    |------------|------------------------------|
    | Brown      | 14(GND)                      |
    | Red        | 4 (5v power)                 |
    | Yellow     | 13(GPIO 27 on Pi-4)          |
    ---------------------------------------------


Advanced Users
==============
The rpi.GPIO library from Rasberry Pi has been encapsulated within the servo package. For now, the GPIO interface 
has not been exposed to the user and the GPIO.cleanup() is performed automatically when the last servo is shutdown().
At a leter state, I might move the GPIO functions into another package when I do stepper motors and other motor
controls.

Setting up servo motor duty cycle to control angles
----------------------------------------------------
A duty cycle or power cycle is the fraction of one period in which a signal or system is active [https://en.wikipedia.org/wiki/Duty_cycle]

The angle of the servo motor is controlled by sending pulses to it. The angle of the motor is set by what is called the duty of the PWM. 
In most common servo motors a duty cycle of 2.0 sets the motor to 0 degrees and a duty cycle of 12.5 for 180 degrees. However the actual duty cycle for each servo 
motor varies from servo motor to servo motors. My servos seem to operate in a range of 2.0 and 10.5 and hence the libarary default range is
from 2.0 to 10.5.

If the above paragraph does not make any sense, don't worry. The process of setting up the servos has been simplified for command line use. 
The instructions for use of a different servo motor and determining duty cycle are as follows: 
1. Wire up the servo motor as per instructions shown above (let's say we wired up on GPIO pin 11, rest of insructions are for pin 11)
2. From the home directory of this project, run the following command:
**python3 -m motor --pin=11 --duty=2.0***
3. Observe the motor position. Change the value of duty cycle till you observe the stepper motor is at position zero. Note that the motor will not rotate any further if you keep decreasing the value of duty cycle.Take the highest value of duty cycle when the angle is still zero.
4. Repeat the same steps to get the corresponding value of duty cycle till you get closest to 180 degress
5. While developing the python code, instatiate the servo object as per the following code:
**s1 = servos.servo(pin=11, min=2.0,max=10.5,waitTime=0.5)**

Rest of the code remains unchanged

Disclaimers
===========
1. As is software. Please let me know any feature requests.
2. It's not the nest software in the world, take it with a pinch of salt.


