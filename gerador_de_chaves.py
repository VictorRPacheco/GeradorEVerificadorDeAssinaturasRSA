import random
from datetime import datetime

def gerandoChaves():
    print(f"{datetime.now()} STATUS: Gerando chaves")

    primo_um = find_nearest_prime(random.randint(0000, 9999))
    primo_dois = find_nearest_prime(random.randint(0000, 9999))

    n = primo_um * primo_dois

    # the totient
    phi_n = (primo_um-1) * (primo_dois-1)

    e = find_e(n, phi_n)
    d = find_d(primo_um, n, e, phi_n)

    return([[n, e], [n, d]])


def checkPrimo(n):
    for val in range(2,n):
        if n % val == 0:
            return False
    return True

def find_nearest_prime(num):
    while num < 100000:
        if checkPrimo(num):
            return num
        else:
            num += 1

def get_factors(num):
    factors = []
    for i in range(2,num):
        if ((num % i) == 0):
            factors.append(i)
    return factors

def isCoprime(num1,num2):
    num1_factors = get_factors(num1)
    num2_factors = get_factors(num2)

    if set(num1_factors).isdisjoint(set(num2_factors)):
        # print('no common factors - they coprime!')
        return True
    else:
        # print('there are common factors, not coprime')
        return False

def find_e(n, phi_n):
    while True:
        if checkPrimo(n):
            if (isCoprime(n, phi_n)):
                return(n)
        else:
            n = n+1

def find_d(prime1, n, e, phi_n):
    for i in range(prime1, n):
        if (((i * e) % phi_n) == 1):
            return i