# Sum of even fibonaccis below 4 million

total = 0
cf = 1
pf = 1
while cf <= 4*(10**6):
    cf, pf = cf + pf, cf
    if cf % 2 == 0:
        total += cf 
    

print(total)
