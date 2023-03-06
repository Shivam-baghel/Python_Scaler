"""
Q3. Distinct Prime
You have given an array A having N integers. Let say G is the product of all elements of A.
You have to find the number of distinct prime divisors of G.

Input Format
The first argument given is an Array A, having N integers.
Output Format
Return an Integer, i.e number of distinct prime divisors of G.

Constraints
1 <= N <= 1e5
1 <= A[i] <= 1e5
For Example
Input:
    A = [1, 2, 3, 4]
Output:
     2
Explanation:
    here G = 1 * 2 * 3 * 4 = 24
    and distinct prime divisors of G are [2, 3]
"""
""" 
my idea here is get the max element from the given array, create a prime array from that max element.
Iterate over the given array and check for every element that how many prime no divisor that element has. and put all those prime no. divisor in an hashset.
return total count of hashset.
"""
import math
# def factor(number):
#     root = int(math.sqrt(number))
#     # the for loop is to check the num is prime or not if prime it returns True else False.
#     # for i in range(2,root+1):
#     #     if num%i==0:
#     #         return False
#     # return True
#     for i in range(number+1):
#         if number%i == 0:
#             return
        
def distinctPrime(A:list):
    num = max(A)
    primeArray = [True]*(num+1)
    primeArray[1] = False
    primeArray[0] = False 
    
    for i in range(2,num+1):
        if primeArray[i] == True:
            for j in range(2*i,num+1,i):
                primeArray[j] = False
                
    hashSet = set()
    for j in range(len(A)):
        for k in range(2,A[j]+1):
            if A[j]%k == 0 and primeArray[k] == True:
                hashSet.add(k)
    
    return len(hashSet)

A = [ 96, 98, 5, 41, 80 ]
print(distinctPrime(A))