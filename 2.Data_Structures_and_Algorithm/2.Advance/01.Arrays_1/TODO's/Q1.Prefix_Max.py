""" 
Q1. Prefix Max
given an array[n]. Construct prefix Max[N] such that prefix Max[i] = max of all elements [0-i]
"""

def prefixMax(array):
    n = len(array)
    prefix =[0]*n
    prefix[0] = array[0]
    maxtillnow = array[0]
    for i in range(1,n):
        prefix[i]=max(maxtillnow,array[i])
        maxtillnow=max(maxtillnow,array[i])
    
    return prefix

a = [1,-6,3,2,8,7]

print(prefixMax(a))