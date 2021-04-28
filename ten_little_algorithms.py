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


def rpmul(a,b):
    """Russian peasant multiplication.
    
    Simple multiplication on shifters, taken from "Ten Little Algorithms" by
    Jason Sachs.

    Args:
        a (int): the first variable,
        b (int): the second vairable.

    Returns:
        x (int): result of multiplication a*b.

    """
    result = 0
    while b != 0:
        if b & 1:
            result += a
        b >>= 1
        a <<= 1
        
    return result

def rpexp(a,b):
    """Russian peasant exponention.
    
    Exponention based on Russian peasant multiplication algorithm, 
    taken from "Ten Little Algorithms" by Jason Sachs.

    Args:
        a (int): the base,
        b (int): the exponent.

    Returns:
        x (int): the b power of a, a**b.

    """
    result = 1
    while b != 0:
        if b & 1:
            result *= a
        b >>= 1
        a *= a
    return result

def sp_iir_lpf(cutoff = 0.25, smpl_f = 1):
    """Single-pole IIR low-pass filter.
    
    A single-pole IIR filter design y += alpha * (x-y), 
    taken from "Ten Little Algorithms" by Jason Sachs.

    Args:
        cutoff (float): the cutoff frequency, can bi in proportion of sampling
                        frequency or in hertz if sampling frequency is given as 
                        second argument
        smpl_f (float): sampling frequency in hertz (optional).

    Returns:
        alpha (float):  filter coefficient alpha,
        h (ndarray):    the frequency response as complex numbers,
        w (ndarray):    the frequencies at which h was computed 
                        in proportion of pi

    """
    import numpy as np
    from scipy import signal
    
    def do_filter(x, alpha, x0 = None):
        y = []
        yk = x[0] if x0 is None else x0
        for k in range(len(x)):
            yk += alpha * (x[k]-yk)
            y.append(yk)
        return y
    
    # calculate coefficient
    dt = 1/smpl_f
    tau = 1 / cutoff
    alpha = dt/tau
    
    # make test impulse signal 
    smpls = np.zeros(1000)
    smpls[0] = 1
    filter_result = do_filter(smpls, alpha)
    
    # get the frequency and phase response with help of scipy
    w, h = signal.freqz(filter_result)
    # change radians to proportions of pi
    for i in range(len(w)):
        w[i] = w[i]/np.pi
    
    return alpha, h, w