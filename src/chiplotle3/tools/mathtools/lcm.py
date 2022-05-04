from __future__ import division
from past.utils import old_div
from math import gcd

def lcm(a, b):
    ''' returns the lowest common multiple of a & b'''
    
    the_gcd = 0
    lcm = 0
    
    if a > b:
        dividend = a
        divisor = b
    else:
        dividend = b
        divisor = a
        
    the_gcd = gcd(dividend,divisor)
    lcm = old_div((a * b), the_gcd)
    
    return lcm