# smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20
import collections
import time
def primefac(n):
    "finds the prime factorization of the given integer"
    rsf = collections.Counter()
    while n != 1:
        if n % 2 == 0:
            rsf += collections.Counter({2:1})
            n = int(n / 2)
        else:
            for m in range(3,n + 1,2):
                if n % int(m) == 0:
                    rsf += collections.Counter({m:1})
                    n = int(n / m)
                    break
    return(rsf)

def lcmpf(n):
    """finds the prime factorization of the lowest common
    multiple of all numbers from 1 - n"""
    rsf = collections.Counter()
    p = n
    while p > 1:
        rsf = rsf | primefac(p)
        p -= 1
    return(rsf)


def lcmv(n):
    """finds the value of the lowest common
        multiple of all numbers from 1- n"""
    start = time.time()
    primefac = lcmpf(n)
    rsf = 1
    for a, b in primefac.items():
        rsf *= a ** b
    print(time.time() - start)
    return(rsf)
    

    
print(lcmv(20))    
        

