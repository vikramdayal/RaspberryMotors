#!/usr/bin/env python3


# Name: __main__.py
# Author: Vikram Dayal
# main program of the package. Used to calibrate the servo motors
# Usage:
#   python3 -m motors -p <GPIO pin> -d <duty cycle>
# or
#   python3 -m motors --pin=<GPIO pin> --duty=<duty cycle>


import sys, getopt
from motors import servos

def main(argv):
    pin = 0
    duty = 2.0
    try:
        opts, args = getopt.getopt(argv,"hp:d:",["pin=","duty="])
    except getopt.GetoptError:
        print("python3 -m motors -p <GPIO pin> -d <duty cycle>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
           print("python3 -m motors -p <GPIO pin> -d <duty cycle>")
           print("python3 -m motors --pin=<GPIO pin> --duty=<duty cycle>")
           sys.exit()
        elif opt in ("-p", "--pin"):
           pin = int(arg)
        elif opt in ("-o", "--ofile"):
           duty = float(arg)
    print("calibrate pin=", pin, " for duty cycle=",duty)
    if pin == 0:
       print("python3 -m motors -p <GPIO pin> -d <duty cycle>")
       sys.exit()
    servos.calibrate(pin,duty)

if __name__ == "__main__":
   main(sys.argv[1:])