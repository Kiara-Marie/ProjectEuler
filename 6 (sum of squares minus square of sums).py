# finds the differene between the square of the sum and the sum
# of the squares of the first n natural numbers

def ssssd(n):
    sqsf = 0
    ssf = 0
    for k in range(n + 1):
        sqsf += k ** 2
        ssf += k
    return((ssf ** 2)- sqsf)
        
