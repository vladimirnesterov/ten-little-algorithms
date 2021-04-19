# -*- coding: utf-8 -*-
"""
@author: vladimirnesterov
Examples for ten little algorithms
(Ten Little Algorithms by Jason Sachs from here https://www.embeddedrelated.com/showarticle/760.php)
"""

import ten_little_algorithms as tla


print('                      --- *** ---                            ')
print(' --- Euclidean Algorithm to find greatest common divider --- ')
from math import gcd
a=1071
b=462
print('Python gcd function', a,'*', b, '=',gcd(a,b))
print('Euclidean algorithm', a,'*', b, '=',tla.euclidean_gcd(a,b))
print(' --- --------------------------------------------------- --- ')
print('')