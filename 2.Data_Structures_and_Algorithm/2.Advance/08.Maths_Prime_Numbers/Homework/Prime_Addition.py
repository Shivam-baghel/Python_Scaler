
""" 
Q2. Prime Addition
You are given an even number N and you need to represent the given number as the sum of primes. The prime numbers do not necessarily have to be distinct. It is guaranteed that at least one possible solution exists.
You need to determine the minimum number of prime numbers needed to represent the given number.

Input
The first argument contains an integer N,the number you need to represent (2<=N<=10^9).
Output
Return an integer which is the minimum number of prime numbers needed to represent the given number N.

Examples
Input
26
Output
2
Explanation
Testcase 1-
You can represent 26 as: 13+13
So we require minimum of 2 prime numbers to represent the number 26.
"""

def primeAddition(number):
        #  mathmatically every even number is a sum of 2  prime number
        #  ex-  1000 = 997+3
        #  and in ques there is simply said that all test case are even
        #  and greater then 2 so we have to just handle one case of
        #  2 itself;
    if number == 2:
        return 1
    return 2

num = int(input())
print(primeAddition(num))