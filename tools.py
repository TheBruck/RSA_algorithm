
"""
Usefull fonctions for The RSA Algorithm
"""

from math import sqrt

def pgcd_euclid(dividend, divisor):
    "We calculate the greatest common divisor (GCD) using the Euclidean method."
    while divisor != 0:
        remder = dividend % divisor
        dividend,divisor = divisor,remder
    return dividend

def coprime(nbr):
    "We search for a number e that is coprime with n"
    e_coprime = 2
    while pgcd_euclid(e_coprime, nbr) != 1:
        e_coprime += 1
    return e_coprime

def coefficient_bezout(a_nbr,b_nbr):
    "We calculate the Bézout coefficients such that au + bv = gcd(a, b)"
    if b_nbr == 0:
        return (1,0)
    (u_nbr, v_nbr) = coefficient_bezout(b_nbr, a_nbr % b_nbr)
    return (v_nbr, u_nbr - (a_nbr // b_nbr) * v_nbr)

def puissance_int(n_nbr, u_nbr):
    "We calculate u raised to the power of n"
    k_nbr = 1
    for _ in range(n_nbr):
        k_nbr = k_nbr * u_nbr
    return k_nbr

def mult_inv(e_nbr, r_nbr):
    "We calculate the inverse of e in Z/rZ"
    _ , s_nbr = coefficient_bezout(e_nbr,r_nbr)
    return s_nbr % r_nbr

## Key Creation

def prime_test(prime):
    "We test if the input integers are prime"
    boo = True
    if boo:
        for i in range(2, int(sqrt(prime))+1):
            if prime % i == 0:
                boo = False
    return boo
