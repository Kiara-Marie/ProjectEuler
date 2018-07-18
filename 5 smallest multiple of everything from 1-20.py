# smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20

def primefac(n):
    "finds the prime factorization of the given integer"
    rsf = []
    while n != 1:
        if n % 2 == 0:
            rsf.append(2)
            n = int(n / 2)
        else:
            for m in range(3,n + 1,2):
                if n % int(m) == 0:
                    rsf.append(m)
                    n = int(n / m)
                    break
    return(rsf)

def lcm(n):
    # finds the 
    
                
                
                
                
            
        
        

