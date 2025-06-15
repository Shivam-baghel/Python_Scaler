""" 
Q2. Suffix Max
given an array[n]. Construct suffix Max[N] such that suffix Max[i] = max of all elements [i-n-1]
"""

def suffixmax(array):
    n = len(array)
    suffix = [0]*n
    suffix[n-1] = array[n-1]
    maxtillnow = array[n-1]
    
    for i in range(n-1,-1,-1):
        suffix[i]= max(maxtillnow,array[i])
        maxtillnow = max(maxtillnow,array[i])
        
    return suffix

a= [3,10,6,7,0,2,-1]
print(suffixmax(a))