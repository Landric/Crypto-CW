""" lfsr.py
    CJ Odenthal
    22/06/2005
    
    Accessed 23/04/2013 from ideone.com/plain/Uz8LR
    
    This module implements some functions dealing with Linear
    Feedback Shift Registers. For details see Section 5.6 of
    "Basic Methods of Cryptography" by J.C.A. van der Lubbe,
    Cambridge University Press (1994).
"""

from operator import xor

def lfsr(coefficients,state=[]):
    """ This implements a LFSR. The inputs are the 'coefficients'
        of the feedback function and the initial 'state' of the
        register.
    """
    # If 'state' is longer than 'coefficients' we'll truncate it.
    # If 'state' is shorter than 'coefficients' we'll pad it with 1s.
    m = len(coefficients)
    state = state[:m]
    state = state + [1]*(m-len(state))

    while 1:
        state.append(dot(coefficients,state))
        yield state.pop(0)


def dot(x,y):
    """ This returns the 'dot' product of the two binary lists
        'x' and 'y'. If either list is empty '0' is returned.
    """
    return reduce(xor,[a&b for (a,b) in zip(x,y)],0)
