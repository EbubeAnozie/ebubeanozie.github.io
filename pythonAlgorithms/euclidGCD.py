"""
Euclid's Algorithm
PURPOSE: Computes the GCD of two natural numbers
"""


def GCD(M, N):
    # Initial state
    x, y = M, N

    # Next state
    while x != y:
        if x < y:
            y = y - x
            continue
        elif y < x:
            x = x - y
            continue
    print(x)
    
GCD(1254, 183)
