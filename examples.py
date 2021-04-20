# -*- coding: utf-8 -*-
"""
@author: vladimirnesterov
Examples for ten little algorithms
(Ten Little Algorithms by Jason Sachs from here https://www.embeddedrelated.com/showarticle/760.php)
"""

import ten_little_algorithms as tla

print('')
print('  --- ----------------------- *** ----------------------- ---  ')
print('   Euclidean Algorithm to find greatest common divider (GCD)   ')
print('')
from math import gcd
a=1071
b=462
print('Python gcd function gcd(', a,',', b, ') =',gcd(a,b))
print('Euclidean algorithm gcd(', a,',', b, ') =',tla.euclidean_gcd(a,b))
print('')

print('  --- ----------------------- *** ----------------------- ---  ')
print(' Extended Euclidean Algorithm to find GCD and Bézouts identity ')
print('')
a=462
b=1071
gdc,x,y = tla.euclidean_ext_gcd(a,b)
print('Euclidean algorithm gcd(', a,',', b, ') =',gdc)
print('Coefficients of Bézouts identity:',x, 'and', y)
print('such that ',a, '*', x, '+', b, '*', y, '=', a*x+b*y)
print('')