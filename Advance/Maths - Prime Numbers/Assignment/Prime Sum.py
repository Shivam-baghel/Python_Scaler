""" 
Q2. Prime Sum
Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to the given number.
If there is more than one solution possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then 
[a, b] < [c, d], If a < c OR a==c AND b < d. 
NOTE: A solution will always exist. Read Goldbach's conjecture.

Problem Constraints
4 <= A <= 2*107

Input Format
First and only argument of input is an even number A.
Output Format
Return a integer array of size 2 containing primes whose sum will be equal to given number.

Example Input
 4
Example Output
 [2, 2]

Example Explanation
 There is only 1 solution for A = 4.
"""

def primeSum(A):
    
    num = A
    # we are first creating a array which will hold if the index is prime or not. time complexity for it will be N*logn.
    primeArray = [True]*(num+1)
    primeArray[1] = False
    primeArray[0] = False
    
    for i in range(2,num+1):
        # we interate on multiples of i if i is prime number
        if (primeArray[i] == True):
            # i is prime. Iterate on multiples of i till n.
            for j in range(2*i,num+1,i):
                primeArray[j] = False
    
    # we have already created a array which holds the if the number is prime or not it is similar to prefix sum array.
    # we will iterate on the primeArray to check a num and A-num is prime or not if yes we will return.
    for k in range(1,num+1):
        if primeArray[k] == True and primeArray[A-k] == True:
            return [k,A-k]

num = int(input())
print(primeSum(num))