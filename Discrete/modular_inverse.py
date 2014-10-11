#!/usr/bin/env python3
##
# Extended Euclidean algorithm to find the modular inverse.
# Source: http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
#

import sys;

##
# Extended GCD
#
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

##
# Modular inverse with Extended Euclidean algorithm.
#
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

##
# Main
#
if len(sys.argv) != 3:
    print("usage: " + sys.argv[0] + " <a> <modulo>");
    quit()

a = int(sys.argv[1])
mod = int(sys.argv[2])
inv = modinv(a, mod)
print(inv)