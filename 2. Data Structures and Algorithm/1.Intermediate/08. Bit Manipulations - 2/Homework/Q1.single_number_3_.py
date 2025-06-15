""" 
Q1. Single Number III

Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
Find the two integers that appear only once.

Note: Return the two numbers in ascending order.

Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109

Input Format
The first argument is an array of integers of size N.

Output Format
Return an array of two integers that appear only once.

Example Input
Input 1:
A = [1, 2, 3, 1, 2, 4]
Input 2:
A = [1, 2]

Example Output
Output 1:
[3, 4]
Output 2:
[1, 2]


Example Explanation

Explanation 1:
3 and 4 appear only once.
Explanation 2:

1 and 2 appear only once.
"""


def singleNumber3(A):
    A.sort()
    res = []
    i = 0
    # for i in range(len(A)-1):
    while i <= (len(A) - 1):

        if i == len(A) - 1:
            if A[i] != A[i - 1]:
                res.append(A[i])
        else:
            if A[i] == A[i + 1]:
                i += 1

            else:
                res.append(A[i])

        i += 1

    return res
