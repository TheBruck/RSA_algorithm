
""" This moduls encrypt and decrypt messages with RSA Algorithm"""

from tools import puissance_int, coprime, coefficient_bezout

def encryption(stri, n_big, e_inv):
    "str: string to be encrypted, (n,e): Public Key."
    list_encrypted = []
    ind = 0
    for char in stri:
        if char.isspace():
            list_encrypted.append(400)
        elif char.islower():
            list_encrypted.append(ord(char) - 97)
            list_encrypted[ind] = puissance_int(e_inv, list_encrypted[ind]) % n_big
        elif char.isupper():
            list_encrypted.append(ord(char) - 65)# ascii
            list_encrypted[ind] = puissance_int(e_inv, list_encrypted[ind]) % n_big # l[i]^^e  [n]
        ind += 1
    return list_encrypted

def decryption(list_encrypted, p_prime, q_prime):
    "list_encrypted: Message to be decrypt, (p_prime, q_prime): Private Key"
    r_private = (p_prime - 1) * (q_prime - 1)
    e_inv = coprime(r_private)
    d_nbr, _ = coefficient_bezout(e_inv, r_private)
    stri = ''
    if d_nbr < 0:
        d_nbr = d_nbr % r_private
    for cha in list_encrypted:
        if cha == 400:
            stri += ' '
        else:
            stri += chr((puissance_int(d_nbr, cha) % (p_prime*q_prime)) + 65)
    return stri

if __name__ == '__main__':
    STRI1 = 'HELLO'
    lis = encryption(STRI1, 5141, 5)
    print(lis)
    print(decryption(lis, 53, 97))
