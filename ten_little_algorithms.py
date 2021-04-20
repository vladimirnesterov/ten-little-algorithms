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
        a,b = b,a
    
    while a > b:
        a = a - b
        
    if (a != b):
        a = euclidean_gcd(b, a)
        
    return a


def euclidean_ext_gcd(a,b):
    """Extended Euclidean Algorithm to find GCD and Bézout's identity.
    
    Extended Euclidean algorithm is an extension to the Euclidean algorithm, 
    and computes, in addition to the greatest common divisor (GCD) of integers 
    a and b, also the coefficients of Bézout's identity, which are integers 
    x and y such that ax+by = gcd(a,b) [Wiki].

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        tuple(int,int,int): the gcd and coefficients x and y.

    """
    def calc_next_step(a,b,s,spv,t,tpv):

        if a < b:
            a,b = b,a
    
        r = a
        qs = 0
        qt = 0
        while r >= b:
            r = r - b
            qs += s
            qt += t
          
        spv, s = s, spv - qs
        tpv, t = t, tpv - qt
        
        return (b, r, s, spv, t, tpv )
    
    spv = 1
    tpv = 0
    s = 0
    t = 1

    flip = 0
    if a < b:
        flip = 1
    
    while (b != 0):
        a,b,s,spv,t,tpv = calc_next_step(a,b,s,spv,t,tpv)
        
    return (a,tpv,spv) if flip else (a,spv,tpv)