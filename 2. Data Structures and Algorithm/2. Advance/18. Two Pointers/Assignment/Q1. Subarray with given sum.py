""" 
Q1. Subarray with given sum

Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
If the answer does not exist return an array with a single element "-1".
First sub-array means the sub-array for which starting index in minimum.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".

Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
 B = 5
Input 2:

 A = [5, 10, 20, 100, 105]
 B = 110


Example Output
Output 1:

 [2, 3]
Output 2:

 -1


Example Explanation
Explanation 1:

 [2, 3] sums up to 5.
Explanation 2:

 No subarray sums up to required number.
"""

def solve(A, B):
    array = A
    n = len(A)
    p1 = 0
    p2 = 0
    totalSum = 0
    while p2 < n:
        # totalSum = array[p1]+array[p2]
        if p1 > p2:
            p2 = p1
            totalSum = array[p2]
        if totalSum == B:
            return array[p1:p2]
        elif totalSum > B:
            totalSum -= array[p1]
            p1 += 1
        else:
            totalSum += array[p2]
            p2 += 1
    
    return -1


A = [1, 2, 3, 4, 5]
B = 5
print(solve(A,B))