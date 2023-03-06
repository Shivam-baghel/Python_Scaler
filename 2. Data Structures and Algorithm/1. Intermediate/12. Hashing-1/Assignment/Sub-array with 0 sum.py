"""
Q4. Sub-array with 0 sum
Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
If the given array contains a sub-array with sum zero return 1, else return 0.

Problem Constraints
1 <= |A| <= 100000
-10^9 <= A[i] <= 10^9

Input Format
The only argument given is the integer array A.

Output Format
Return whether the given array contains a subarray with a sum equal to 0.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [-1, 1]

Example Output
Output 1:
 0
Output 2:
 1

Example Explanation
Explanation 1:
 No subarray has sum 0.
Explanation 2:
 The array has sum 0.
"""

def subArrayWithZeroSum(A):
    prefixSum = [0]*len(A)
    hs = set()     #this hashSet declaration
    prefixSum[0] = A[0]
    hs.add(prefixSum[0])
    for i in range(1,len(A)):
        prefixSum[i] = prefixSum[i-1] + A[i]
        hs.add(prefixSum[i])
    
    if len(hs)<len(A) or (0 in hs):
        return 1
    else:
        return 0

A = [1, 2, 3, 4, 5]
print(subArrayWithZeroSum(A))