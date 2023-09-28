""" 
Longest Consecutive Sequence

Given an unsorted integer array A of size N.

Find the length of the longest set of consecutive elements from array A.

Problem Constraints
1 <= N <= 106
-106 <= A[i] <= 106

Input Format
First argument is an integer array A of size N.

Output Format
Return an integer denoting the length of the longest set of consecutive elements from the array A.

Example Input
Input 1:

A = [100, 4, 200, 1, 3, 2]
Input 2:

A = [2, 1]

Example Output
Output 1:

 4
Output 2:

 2


Example Explanation
Explanation 1:

 The set of consecutive elements will be [1, 2, 3, 4].
Explanation 2:

 The set of consecutive elements will be [1, 2].
"""


# @param A : tuple of integers
# @return an integer
def longestConsecutive(A):
    lst = A
    if not lst:
        return 0
    
    lstSet = set(lst)
    mlen = 0
    
    for i in lstSet:
        if i-1 not in lstSet:
            curr_num = i
            curr_len = 1
            
            while curr_num + 1 in lstSet:
                curr_num +=1
                curr_len +=1
            
            mlen = max(mlen,curr_len)
    return mlen


A = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(A))