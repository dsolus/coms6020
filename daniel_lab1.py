#!usr/bin/env python3.5
#Daniel Solus
#Lab 1 - fraction to mixed number converter
"""This program asks for a numerator and denominator. Performs division and
outputs a mixed number. This task is repeated 3 times."""
from fractions import Fraction

def frac_converter():
    #input
    num = input("please enter the numerator: ")
    den = input("please enter the denominator: ")

    #calculating integer fraction and remainder
    num = int(num)
    den = int(den)
    frac = num//den
    remainder = (num % den)

    #output in string datatype
    return print("mixed number:", str(frac) + ' ' +  str(remainder) + '/' + str(den))

n = 0
while n < 3:
    frac_converter()
    n += 1

