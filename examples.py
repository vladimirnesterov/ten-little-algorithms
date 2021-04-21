# -*- coding: utf-8 -*-
"""
@author: vladimirnesterov
Examples for ten little algorithms
(Ten Little Algorithms by Jason Sachs from here https://www.embeddedrelated.com/showarticle/760.php)
"""

import ten_little_algorithms as tla

print("")
print("  --- ----------------------- *** ----------------------- ---  ")
print("   Euclidean Algorithm to find greatest common divider (GCD)   ")
print("")
from math import gcd
a=1071
b=462
print("Python gcd function gcd(", a,",", b, ") =",gcd(a,b))
print("Euclidean algorithm gcd(", a,",", b, ") =",tla.euclidean_gcd(a,b))
print("")

print("  --- ----------------------- *** ----------------------- ---  ")
print(" Extended Euclidean Algorithm to find GCD and Bézout's identity ")
print("")
a=462
b=1071
gdc,x,y = tla.euclidean_ext_gcd(a,b)
print("Euclidean algorithm gcd(", a,",", b, ") =",gdc)
print("Coefficients of Bézout's identity:",x, "and", y)
print("such that ",a, "*", x, "+", b, "*", y, "=", a*x+b*y)
print("")

print("  --- ----------------------- *** ----------------------- ---  ")
print("              Newton's method for finding roots                ")
print("")
from scipy import optimize

def f(x: float) -> float:
    return x**2 - 20 * x + 5

def f_derivative(x: float) -> float:
    return 2 * x - 20

x0 = 100 #1
eps = 1e-7
kmax =1e3

newton_result = tla.newton(f, f_derivative, x0, eps, kmax)    
scipy_result = optimize.root(f, x0)

print("Test function is (x^2 - 20*x + 5), first guess is", x0)
print("Newton's method for finding root =",newton_result, "f(newton root)=", f(newton_result))
print("Scipy function for finding roots =",scipy_result.x[0], "f(scipy root)= ", f(scipy_result.x[0]))
print("")