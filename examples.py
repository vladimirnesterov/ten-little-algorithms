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

print("  --- ----------------------- *** ----------------------- ---   ")
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
print("Newton's method root =",newton_result, ", f(newton root)=", f(newton_result))
print("Scipy function roots =",scipy_result.x[0], ", f(scipy root)= ", f(scipy_result.x[0]))
print("")

print("  --- ----------------------- *** ----------------------- ---  ")
print("                  Russian Peasant algorithm                    ")
print("")
a=462
b=1071
mul_result = tla.rpmul(a,b)
print("Russian Peasant Multiplication ", a,"*", b, "=",mul_result)
print("Correct is:", a*b)
a=2
b=23
exp_result = tla.rpexp(a,b)
print("Russian Peasant Exponentiation ", a,"**", b, "=",exp_result)
print("Correct is:", a**b)
print("")


print("  --- ----------------------- *** ----------------------- ---  ")
print("                The Single-Pole Low-Pass Filter                ")
print("")

import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np

cutoff_freq = 2000
smpl_freq = 8000

alpha, h, w = tla.sp_iir_lpf(cutoff_freq, smpl_freq)

# Plot example is from scipy.signal.freqz function description
fig, ax1 = plt.subplots()
ax1.set_title('SP IIR filter frequency responses with cutoff frequency = '+str(cutoff_freq/(2*smpl_freq))+'$\pi$')
    
ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid()
ax2.axis('tight')
ax2.xaxis.set_major_formatter(ticker.FormatStrFormatter('%g $\pi$'))
ax2.xaxis.set_major_locator(ticker.MultipleLocator(base=0.25))
plt.show()

print("The single-pole IIR low-pass filter with cutoff frequency", cutoff_freq,"\nhas coefficient alpha =",alpha)
print("See the frequency response on the figure.")
print("")


print("  --- ----------------------- *** ----------------------- ---  ")
print("                Statistic and Welford's method                 ")
print("")
import test_signals as ts
w_mean, w_var = tla.welford(ts.noise_signal)
np_mean = np.mean(ts.noise_signal)
np_var = np.var(ts.noise_signal, ddof=1)
print("Welford:", w_mean, w_var)
print("numpy:  ", np_mean, np_var)
print("")