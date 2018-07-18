# 10,001st prime
import math
def isPrime(n):
    "produces true if given number is prime"
    prime = True
    for pos in range(2,int(math.sqrt(n))+ 1):
            if n % pos == 0:
                prime = False
                break
    return(prime)


def nthPrime(n):
    "produces the nth prime"
    c = 2
    k = 3
    while c < n:
        if isPrime(k):
            c += 1
            k += 1
        else:
            k += 1
    while True:
        if isPrime(k):
            return(k)
        else:
            k += 1
    
    
