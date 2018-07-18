# finds pythagorean triple a,b,c whose sum = 1000

for a in range(1,1000):
    for b in range(1,1000):
        c = ((a ** 2) + (b ** 2)) ** 0.5
        if c % int(c) == 0:
            if a + b + c == 1000:
                print (a, b, c, a * b * c)
                break 
