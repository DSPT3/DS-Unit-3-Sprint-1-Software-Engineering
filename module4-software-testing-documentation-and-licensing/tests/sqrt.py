''' A function the takes the quare root of a number '''

from numpy.testing import assert_almost_equal as eq 
from math import sqrt

def newton_sqrt1(x):
    '''Return the square root of x using Newton;s Method'''
    val = x
    while True:
        last = val
        val = (val + x/val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val

def newton_sqrt2(x, guess=2):
    '''Danger! Something's not quite right'''
    if eq(newton_sqrt2(x, guess)**2, x):
        return guess
    else:
        guess = 0.5*(guess+x)
        
def lazy_sqrt(x):
    '''1 of 2 most common'''
    return x**0.5

def builtin_sqrt(x):
    '''2 of 2 most common'''
    return sqrt(x)
