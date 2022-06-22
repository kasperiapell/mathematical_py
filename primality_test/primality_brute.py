import math

def primality_brute (n):
    if (n <= 1):
        return False
    else:
        m = 2
        while m <= math.sqrt(n):
            if (n % m == 0):
                return False
                break
            else:
                m = m + 1
        return True