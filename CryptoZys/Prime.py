import math
import secrets
from random import randrange

class Prime():
    def __init__(self):
        pass


    @staticmethod
    def is_prime(n):
        bound = math.ceil(math.sqrt(n))

        for i in range(2, int(bound)):
            if n % i == 0:
                return False

        return True
        
    
    @staticmethod
    def is_prime_mr(n, k=128):
        # Test if n is not even.
        # But care, 2 is prime !
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        # find r and s
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        # do k tests
        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True


    @staticmethod
    def get_rand_prime(bits=1024, tests=128):
        pot_prime = secrets.randbits(bits)
        while not Prime.is_prime_mr(pot_prime, tests):
            pot_prime = secrets.randbits(bits)

        return pot_prime
