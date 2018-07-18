# Find largest prime factor
n = 1301081

factors = []

for val in list(range (int(n ** 0.5)))[:: -1]:
    if n % val == 0: 
        for pos in range(2,val):
            if val % pos == 0:
                prime = False
                break
            else:
                prime = True
        if prime:
            answer = val
            break
        

print(answer) 
        
        
    
