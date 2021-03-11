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

def find_prime_factors(number):
    """ Esta función devuelve los factores primos de un número como una lista"""
    prime_factor_list = []
    while number % 2 == 0:
        prime_factor_list.append(2)
        number /= 2

    factor = 3 
    while number != 1:
        if number % factor == 0:
            prime_factor_list.append(factor)
            number /= factor
        else:
            factor += 2
    return prime_factor_list

def main():
    check_input()

    denominator = 10000
    numerator = round(float(sys.argv[1]) * denominator)
    
    denominator_prime_factor_list = find_prime_factors(denominator)

    for prime_factor in denominator_prime_factor_list:
        if numerator % prime_factor == 0:
            numerator /= prime_factor
            denominator /= prime_factor

    print(int(numerator), '/', int(denominator))

main()
