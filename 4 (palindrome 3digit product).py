def isPalindrome(x):
    "Produces true if the given number is a palindrome"
    sx = str(x) # a string version of the given number
    lx = len(sx) # the number of digits in the given number
    n = lx - 1
    m = 0
    while 5 == 5:
        if sx[m] != sx[n] :
            return (False)
            break
        elif m >= n:
            return (True)
            break
        else:
            n -= 1
            m += 1

#Program to find biggest palindrome made by multiplying 2 3-digit numbers

n = 100
m = 100
rsf = -1
x = -1
for n in range(999):
    for m in range(999):
        if (m * n) > x and isPalindrome(m * n):
            rsf += 1
            x = m * n
            
        
print(rsf,x)

