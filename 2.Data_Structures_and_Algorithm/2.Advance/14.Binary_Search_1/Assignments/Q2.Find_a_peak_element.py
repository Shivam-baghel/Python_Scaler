""" 
Q2. Find a peak element

Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.
For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.
NOTE: Users are expected to solve this in O(log(N)) time. The array may have duplicate elements.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 109

Input Format
The only argument given is the integer array A.

Output Format
Return the peak element.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
Input 2:
A = [5, 17, 100, 11]

Example Output
Output 1:
 5
Output 2:
 100

Example Explanation
Explanation 1:
 5 is the peak.
Explanation 2:
 100 is the peak.
"""

def solve(A):
    n = len(A)
    if n>=2:
        if A[0]>A[1]:
            return A[0]
        if A[n-2]<A[n-1]:
            return A[n-1]

        l = 1
        h = n-1

        while(l<=h):
            m = (l+h)//2
            if A[m-1]<=A[m] and A[m]>=A[m+1]:
                return A[m]
            elif A[m-1]<A[m]:
                l=m+1
            else:
                h=m-1
    else:
        return A[0]