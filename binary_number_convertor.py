#  
# Copyright (c) Brian C. Welch. www.brianwelch.se
# All rights reserved.  
# Licensed under the MIT License.
# Personas arae free to reproduce this code provided
# they do not removed this header
# + + + + + + + + + + + + + + + + 

def binary_calc(digit_in):
    '''this one took a while - converting an integer into a binary'''
    binary_digit1 = []
    while digit_in > 0:
        binar = digit_in%2
        binary_digit1 += str(binar)
        digit_in = int(digit_in / 2)
    binary_length = int(len(binary_digit1))
    output = ""
    while binary_length > 0:
        output += binary_digit1[binary_length - 1]
        binary_length = binary_length - 1
    return output
