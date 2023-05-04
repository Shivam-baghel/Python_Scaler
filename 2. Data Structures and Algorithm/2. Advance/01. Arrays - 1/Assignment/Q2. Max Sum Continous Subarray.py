""" 
Q2. Max Sum Contiguous Subarray
Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.


Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000

Input Format
The first and the only argument contains an integer array, A.

Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.

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
 The subarray [4,-1,2,1] has the maximum possible sum of 6.
"""


def maxSubArray(A):
    largestSum = -float('inf')
    # for i in range(len(A)):
    #     sumofElements = 0
    #     for j in range(i,len(A)):
    #         sumofElements = sumofElements + A[j]            
    #         largestSum = max(largestSum,sumofElements)
    max_sum_till = float('-inf')
    for i in range(len(A)):
        if(max_sum_till<0):
            max_sum_till = A[i]
        else:
            max_sum_till += A[i]

        if largestSum<max_sum_till:
            largestSum = max_sum_till
    
    return largestSum