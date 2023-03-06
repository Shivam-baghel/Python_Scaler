""" 
Print all prime nombers from 1 - N.
ex:
n = 10
output: 2,3,5,7
"""
def allPrime(num):
    primeArray = [True]*(num+1)
    primeArray[1] = False
    primeArray[0] = False
    
    for i in range(2,num+1):
        # we interate on multiples of i if i is prime number
        if (primeArray[i] == True):
            # i is prime. Interate on multiples of i till n.
            for j in range(2*i,num+1,i):
                primeArray[j] = False
    
    for k in range(2,num+1):
        if primeArray[k] == True:
            print(k,end=" ")
            
number = int(input())
allPrime(number)