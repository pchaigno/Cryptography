#!/usr/bin/env python3
##
# RSA decryption by computing the private key exponent.
# This version needs the prime numbers.
#

import sys;

##
# Computes Euler's totient function value for the modulus.
#
def euler_totient(p1, p2):
    return (p1 - 1) * (p2 - 1)

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
if len(sys.argv) < 6:
    print("Usage: " + sys.argv[0] + " <ciphertext> <public key exponent> <modulus> <prime factor 1> <prime factor 2>...");
    quit()

ciphertext = int(sys.argv[1])
e = int(sys.argv[2])
n = int(sys.argv[3])
p1 = int(sys.argv[4])
p2 = int(sys.argv[5])

if p1 * p2 != n:
    print("Incorrect prime factors.")
    exit()

phi = euler_totient(p1, p2)
print("phi(n) = " + str(phi))
d = modinv(e, phi)
print("d = " + str(d))
plaintext = pow(ciphertext, d, n)
print("plaintext = " + str(plaintext))