# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:57:04 2017

@author: Play
"""
stillSearching = True
triNum = 1
curNatural = 1
curNumDivisors = 1

          
def numDivisors(n):
    if ((n**0.5 - int(n ** 0.5)) < 0.00001):
        ret = -1
    else:
        ret = 0
    for val in range(1,int(n**0.5) + 1):
        if (n%val == 0):
            ret += 2
    return(ret)


            
"""
while (stillSearching):
    curNumDivisors = max (curNumDivisors, numDivisors(triNum))
    if (curNumDivisors > 500):
        print(triNum,curNumDivisors)
        stillSearching = False
    else :
        triNum += curNatural
        curNatural += 1

"""
        
n = 1        
while (stillSearching):
    curNumDivisors = max (curNumDivisors, numDivisors((n*(n+1)*0.5)))
    if (curNumDivisors > 500):
        print(n*(n+1)*0.5,curNumDivisors)
        stillSearching = False
    else :
        n += 1
        
        
        
    