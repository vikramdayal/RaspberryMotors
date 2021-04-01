# RasberryServo

Welcome to my Rasberry Pi service library. In this library I have started with an interface to control
sevro motors using the GPIO pins of the Rasberry pi. The driver for me to write the this library was that all
internet examples of using servos on Rasberry were too painful to set up PWM and claculate duty! I wanted to 
control several servo motors simulatenously and was missing the quiet elegance on the Arduino Servo library.

If you want to figure out how to use my library, I would suggest
that you start by using the examples in the sequence provided below:

1. example_simple_servo.py
2. example_simple_2servos.py
3. example_timer_servo.py

By the time you are done with the third example, you should find that you can do pretty much anything with
Rasberry Pi and the Servo library.

Wiring required to run the example
==================================

The examples require two servo motors, I used Vilros SG90 (9g) and MicroServo DXW90 (9g) servos. Please feel free 
to use your own. Keep in mind if you are using the bigger servos you would have to power them sepearetly. The internet
is full of examples of how to wire up servos. In my example the wiring is very simple, to minimise power ports and segregate
power suppoy for the servos, feel free to use a breadboard instead:

 servo-1 (refered to S1 in the example code)
 -------------------------------------------
 
    ---------------------------------------------
    | servo wire | connected to GPIO port on Pi |
    |------------|------------------------------|
    | Brown      | 6 (GND)                      |
    | Red        | 2 (5v power)                 |
    | Yellow     | 11(GPIO 17 on Pi-4)          |
    ---------------------------------------------


 servo-2 (refered to S2 in the example code)
 -------------------------------------------
 
    ---------------------------------------------
    | servo wire | connected to GPIO port on Pi |
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

Disclaimers
===========
1. As is software. Please let me know any feature requests.
2. It's not the nest software in the world, take it with a pinch of salt.


