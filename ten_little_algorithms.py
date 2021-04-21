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
        a (int): The first integer, > 0,
        b (int): The second integer, > 0.

    Returns:
        int: the greatest common divisor.

    """
    if a < b:
        a,b = b,a
    
    while a > b:
        a = a - b
        
    if (a != b):
        #print("a =", a, "b =", b)
        a = euclidean_gcd(b, a)
        
    return a


def euclidean_ext_gcd(a,b):
    """Extended Euclidean Algorithm to find GCD and Bézout's identity.
    
    Extended Euclidean algorithm is an extension to the Euclidean algorithm, 
    and computes, in addition to the greatest common divisor (GCD) of integers 
    a and b, also the coefficients of Bézout's identity, which are integers 
    x and y such that ax+by = gcd(a,b) [Wiki].

    Args:
        a (int): The first integer, > 0,
        b (int): The second integer, > 0.

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
        #print("a =", a, "b =", b, "s =", s, "t =", t)
        a,b,s,spv,t,tpv = calc_next_step(a,b,s,spv,t,tpv)
        
    return (a,tpv,spv) if flip else (a,spv,tpv)

def newton(f, f_derivative, x0, eps, kmax):
    """Newton's method for finding roots.
    
    The Newton's method (Newton–Raphson method) is a root-finding algorithm 
    which produces approximations to the roots (or zeroes) 
    of a real-valued function. [Wiki].

    Args:
        f (function): single-variable function f ,
        f_derivative (function):  the function's derivative f ′,
        x0 (float): initial guess,
        eps (float): precision wanted,
        kmax (int): maximum number of iterations.

    Returns:
        x (float): root of f(x) = 0.

    """
    x = x0
    x_prev = x0 + 2 * eps
    i = 0
	
    while (abs(x - x_prev) >= eps) and (i < kmax):
        #print("Step", i, ":", int(x), int(x_prev), ", x - f(x) = ", int(x - f(x)), ", f_derivative(x) = ", int(f_derivative(x)), "f/f'=",int(f(x)/f_derivative(x)))
        x, x_prev =  x - ( f(x) / f_derivative(x) ), x
        i += 1
        

    return x