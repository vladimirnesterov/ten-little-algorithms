# -*- coding: utf-8 -*-
"""
@author: vladimirnesterov
Ten Little Algorithms by Jason Sachs from here https://www.embeddedrelated.com/showarticle/760.php
"""

def euclidean_gcd(a,b):
    """Euclidean Algorithm to find greatest common divisor.
    
    Euclidean algorithm is an efficient method for computing 
    the greatest common divisor (GCD) of two integers (numbers), 
    the largest number that divides them both without a remainder [Wiki].

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: the greatest common divisor.

    """
    if a < b:
        tmp = b
        b = a
        a = tmp
    
    while a > b:
        a = a - b
        
    if (a != b):
        a = euclidean_gcd(b, a)
        
    return a