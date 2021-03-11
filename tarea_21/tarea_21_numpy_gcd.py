import numpy as np
import sys


def check_input():
    """ Esta función checkea que el input es un número"""
    try:
        float(sys.argv[1])
    except ValueError:
        print('Not a number')
    else:
        if float(sys.argv[1]) > 0.9999 or float(sys.argv[1]) < 0.0001:
            print("Number out of range [0.0001, 0.9999]")
            exit()

def main():

    check_input()

    denominator = 10000
    numerator = round(float(sys.argv[1]) * denominator)

    # Hallar el máximo común divisor 
    mcd = np.gcd(numerator, denominator)

    print(int(numerator/mcd), '/', int(denominator/mcd))

main()
