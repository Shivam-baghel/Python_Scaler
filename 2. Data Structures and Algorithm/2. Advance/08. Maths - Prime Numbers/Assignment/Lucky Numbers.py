"""
Q3. Lucky Number
A lucky number is a number that has exactly 2 distinct prime divisors.
You are given a number A, and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).

Problem Constraints
1 <= A <= 50000
Input Format
The first and only argument is an integer A.
Output Format
Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.

Example Input
Input 1:
 A = 8
Input 2:
 A = 12

Example Output
Output 1:
 1
Output 2:
 3

Example Explanation
Explanation 1:
 Between [1, 8] there is only 1 lucky number i.e 6.
 6 has 2 distinct prime factors i.e 2 and 3.
Explanation 2:
 Between [1, 12] there are 3 lucky number: 6, 10 and 12.
"""


def luckyNumber(A):
    num = A
    primeArray = [0] * (num + 1)
    """ we have created a primeArray of size A+1. this array we are creating with the seive of erthotheisies.
    here we have made some modification to array. instead of making multiples of prime no. false. we will increase the count of that particular no. this will indicate that particular no. is divisible by a prime no. or more prime numbers.
    after this let's say primeArray[6] == 2 that means 6 is divisible by two different prime no.
    now we just have to count the no. of 2's in prime array that is out ans.
    """
    for i in range(2, num + 1):
        # we interate on multiples of i if i is prime number
        if (primeArray[i] == 0):
            # i is prime. Iterate on multiples of i till n.
            for j in range(2 * i, num + 1, i):
                primeArray[j] += 1

    ans = 0
    for k in range(len(primeArray)):
        if primeArray[k] == 2:
            ans += 1

    return ans


inputNumber = int(input())
print(luckyNumber(inputNumber))
