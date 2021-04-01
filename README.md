# RasberryServo

Welcome to a Rasberry Pi service library dedicated to motor control. This library has been started as an interface to control
sevro motors using the GPIO pins on the Rasberry pi. 

The motivation to write the this library was that using servos on Rasberry is too painful. One has to to set up the pluse width modulation (PWM) and claculate duty cycles in order to operate the servos! I also wanted to control several servo motors simulatenously and 
most example were showing how to control one servo at a time. Mostly i missed, the quiet elegance on the Arduino Servo library.

Getting started
===============
Download or clone this site:

1. Make your working directory and change directory (cd) to it
2. Issue the following command:
**git clone https://github.com/vikramdayal/RasberryServo**
3. cd RasberryServo
4. Explore and test

If you want to figure out how to use the library, you might start by using the examples in the sequence provided below:

1. example_simple_servo.py: simple setup and control a single servo
2. example_simple_2servos.py: simple setup and control two servos sequentailly
3. example_timer_servo.py: advanced setup and control two servos simultaneously

By the time you are done with the third example, you should find that you can do pretty much anything with
Rasberry Pi and the Servo library.

Please note that the servos will operate only if they are wired correctly. Simplified instrucions on wiring the servos are provided here.

Wiring required to run the example
==================================

The examples provided here require two servo motors, I used Vilros SG90 (9g) and MicroServo DXW90 (9g) servos. Please feel free 
to use any of your own brands and ratings. Keep in mind if you are using the bigger servos you would have to power them seperately. The internet
is full of examples of how to wire up servos and using breadboards, feel free to follow any of those instructions. Essentially, the main requirement is to connect the control(usually the yellow) wire of the servo to the GPIO pin on the Rasberry.

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
control interfaces.

Setting up servo motor duty cycle to control angles
----------------------------------------------------
A duty cycle or power cycle is the fraction of one period in which a signal or system is active [https://en.wikipedia.org/wiki/Duty_cycle]

The angle of the servo motor is controlled by sending pulses to it. The angle of the motor is set by setting what is called the duty cycle of the PWM. 
In most common servo motors a duty cycle of 2.0 sets the motor to 0 degrees and a duty cycle of 12.5 sets it to 180 degrees. However the actual numbers varies for each servo. My servos seem to operate in a range of 2.0 and 10.5 and hence this libarary has been coded for a default range of
from 2.0 to 10.5.

If the above paragraph does not make any sense, don't worry. The process of setting up the servos has been simplified with a simple command line use. 
The instructions for use of a different servo motor and determining duty cycle are as follows: 
1. Wire up the servo motor as per instructions shown above (let's say we wired up on GPIO pin 11, rest of insructions are for pin 11)
2. From the home directory of this project, run the following command:
**python3 -m motor --pin=11 --duty=2.0***
3. Observe the motor position. Vary the value of duty cycle in the above command till you observe the stepper motor is at position zero. Note that the motor will not rotate any further if you keep decreasing the value of duty cycle.Take the highest value of duty cycle when the angle is still zero.
4. Repeat the same steps in increasing values to get the corresponding value of duty cycle closest to 180 degress
5. In the the python code, instatiate the servo object as per the following code:
**s1 = servos.servo(pin=11, min=2.0,max=10.5,waitTime=0.5)**

Rest of the code remains unchanged

Disclaimers
===========
1. As is software. Please let me know any feature requests.
2. It's not the nest software in the world, take it with a pinch of salt.


