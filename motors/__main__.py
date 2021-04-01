import sys, getopt
from motors import servos

def main(argv):
    port = 0
    duty = 2.0
    try:
        opts, args = getopt.getopt(argv,"hp:d:",["port=","duty="])
    except getopt.GetoptError:
        print("python3 -m motors -p <GPIO port> -d <duty>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
           print("python3 -m motors -p <GPIO port> -d <duty>")
           sys.exit()
        elif opt in ("-p", "--port"):
           port = int(arg)
        elif opt in ("-o", "--ofile"):
           duty = float(arg)
    print("calibrate port=", port, " for duty=",duty)
    if port == 0:
       print("python3 -m motors -p <GPIO port> -d <duty>")
       sys.exit()
    servos.calibrate(port,duty)

if __name__ == "__main__":
   main(sys.argv[1:])
