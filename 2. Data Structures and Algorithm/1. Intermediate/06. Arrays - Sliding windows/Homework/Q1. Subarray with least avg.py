""" 
Q1. Subarray with least average

Given an array A of size N, find the subarray of size B with the least average.

Problem Constraints
1 <= B <= N <= 105
-105 <= A[i] <= 105


Input Format
First argument contains an array A of integers of size N.
Second argument contains integer B.


Output Format
Return the index of the first element of the subarray of size B that has least average.
Array indexing starts from 0.


Example Input
Input 1:
A = [3, 7, 90, 20, 10, 50, 40]
B = 3
Input 2:

A = [3, 7, 5, 20, -10, 0, 12]
B = 2


Example Output
Output 1:
3
Output 2:
4

Example Explanation
Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average 
among all subarrays of size 3.
Explanation 2:

 Subarray between [4, 5] has minimum average
"""


def subarray_least_avg(A: list, B: int):
    res = 0
    summ = 0
    for i in range(B):
        summ += A[i]
    n = len(A)
    min_sum = summ
    for i in range(B, n):
        summ += A[i] - A[i - B]
        if summ < min_sum:
            min_sum = summ
            res = i - B + 1
    return res


if __name__ == '__main__':
    A = [3, 7, 90, 20, 10, 50, 40]
    B = 3
    print(subarray_least_avg(A, B))
