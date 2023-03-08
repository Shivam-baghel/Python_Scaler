""" 
Q3. Subarray with least average
Given an array of size N, find the subarray of size K with the least average.

Problem Constraints
1<=k<=N<=1e5
-1e5<=A[i]<=1e5

Input Format
First argument contains an array A of integers of size N.
Second argument contains integer k.

Output Format
Return the index of the first element of the subarray of size k that has least average.
Array indexing starts from 0.

Example Input
Input 1:
A=[3, 7, 90, 20, 10, 50, 40]
B=3
Input 2:
A=[3, 7, 5, 20, -10, 0, 12]
B=2

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

def leastAvg(A, B):
    # Using sliding window technique.
    
    # set leastAvg to max
    leastAvg = float('inf')
    # length of array
    n = len(A)
    # sum of subarray
    sumof = 0
    # avg of subarray
    avg = 0
    
    # getting sum for subarray window of B
    for i in range(B):
        sumof+=A[i]

    avg = sumof/B
    # getting leastavg
    leastAvg = min(leastAvg,avg)
    # setting avg
    index = 0
    
    for j in range(B,n):
        sumof = sumof+A[j]-A[j-B]
        avg = sumof/B
        if avg < leastAvg:
            leastAvg = avg
            index = j-B+1

    return index

A = [ 20, 1, 5, 2, 7, 5, 17 ]
B = 6
print(leastAvg(A,B))