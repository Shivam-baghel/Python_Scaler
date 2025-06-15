"""
Problem Description:

Given an integer array A of size N. In one second, you can increase the value of one element by 1.
Find the minimum time in seconds to make all elements of the array equal.

Example Input
A = [2, 4, 1, 3, 2]

Example Output
8

Example Explanation
We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.

"""


def timeRequired(A):
    maxValue = -float('inf')
    for i in A:
        if maxValue < i:
            maxValue = i
    count = 0
    for i in range(len(A)):
        count = count + (maxValue - A[i])

    return count


a = tuple(map(int, input().split()))
print(timeRequired(a))
