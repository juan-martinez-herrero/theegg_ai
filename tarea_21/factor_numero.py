#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

def count(number, factor):
    """Función que calcula la ocurrencia de un factor dado un número"""
    counter = 0
    while number % factor == 0:
        counter += 1
        number /= factor
    return counter

def reduce(number, counter, factor):
    """Función que reduce un número por el factor indicado
    "counter" veces hasta un maximo de 4 veces"""
    if counter <= 4:
        reduced_number = number / factor ** counter
    else:
        reduced_number = number / factor ** 4
    return reduced_number

def main():
    import sys

    check_input()

    denominator = 10000
    numerator = round(float(sys.argv[1]) * denominator)

    count2s, count5s = count(numerator, 2), count(numerator, 5)

    reduced2_numerator, reduced2_denominator = reduce(numerator, count2s, 2), reduce(denominator, count2s, 2)
    reduced5_numerator, reduced5_denominator = reduce(reduced2_numerator, count5s, 5), reduce(reduced2_denominator, count5s, 5)

    print(int(reduced5_numerator), '/', int(reduced5_denominator))

main()
