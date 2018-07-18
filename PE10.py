# finds sum of primes below n
import math
def isPrime(n):
    "produces true if given number is prime"
    prime = True
    for pos in range(2,int(math.sqrt(n))+ 1):
            if n % pos == 0:
                prime = False
                break
    return(prime)

def primesBelowNSum(n):
    rsf = 0
    odd = True
    for v in range(n):
        if odd:
            if isPrime(v):
                rsf += v
            odd = False
        else:
            odd = True
    print(rsf - 1)
            
            
