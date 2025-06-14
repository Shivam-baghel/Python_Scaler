"""
Q1. Max Sum Contiguous Subarray
Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.

Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000

Example Input
Input 1:
 A = [1, 2, 3, 4, -10] 
Input 2:
 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 

Example Output
Output 1:
    10 
Output 2:
    6 

Example Explanation
Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
Explanation 2:
    he subarray [4,-1,2,1] has the maximum possible sum of 6.
"""


def maxSubArray(A: tuple):
    largestSum = 0
    for i in range(len(A)):
        sumofElements = 0
        for j in range(i, len(A)):
            sumofElements = sumofElements + A[j]
            largestSum = max(largestSum, sumofElements)

    print(largestSum)


arr = tuple(map(int, input().split()))
maxSubArray(arr)
