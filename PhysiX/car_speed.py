from math import *

"""
a : acceleration
v : speed
x : position
t : time
"""

def acceleration(a0, s0, x0, t):
    a = a0
    s = a0 * t + s0
    x = 1 / 2 * a0 * sqrt(t) + s0 * t + x0
    return a, s, x