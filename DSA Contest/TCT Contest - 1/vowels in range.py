""" 
Vowels in a range

Given a string A of length N consisting of lowercase letters, and Q queries given by the 2D array B of size Q*2. Each query consists of two integers B[i][0] and B[i][1].
For every query, the task is to find the count of vowels in the substring A[B[i][0] … B[i][1]].

Problem Constraints
1 <= N <= 105
1 <= Q <= 105
0 <= B[i][0] <= B[i][1] < N

Input Format
First argument A is a string.
Second argument B is a 2D array of integers.

Output Format
Return an array of integers.


Example Input
Input 1:
A = "scaler"
B = [   [0,2] 
        [2,4]   ]
Input 2:
A = "interviewbit"
B = [   [0,4] 
        [9,10]   ]


Example Output
Output 1:
[1, 2]
Output 2:
[2, 1]


Example Explanation
For Input 1:
The substring for the first query is "sca" which contains 1 vowel.
The substring for the second query is "ale" which contains 2 vowels.
For Input 2:
The substring for the first query is "inter" which contains 2 vowels.
The substring for the second query is "bi" which contains 1 vowel.

"""
def solve(A, B):
    # idea is to get prefix vowel sum of the array
    # use that to get all the list of the count of the vowels in substring
    lst = A
    n = len(lst)
    # prefix vowel sum
    vowelSet = {'a','e','i','o','u','A','E','I','O','U'}
    vlst = [None]*n
    if lst[0] in vowelSet:
        vlst[0] = 1
    else:
        vlst[0] = 0
    
    for i in range(1,n):
        if lst[i] in vowelSet:
            vlst[i] = vlst[i-1]+1
        else:
            vlst[i] = vlst[i-1]
    
    # using prefix vowel sum to count vowels in substring
    ans =[]
    for i in range(len(B)):
        sindex = B[i][0]
        eindex = B[i][1]
        if sindex == 0:
            ans.append(vlst[eindex])
        else:
            count = vlst[eindex]-vlst[sindex-1]
            ans.append(count)
    
    return ans

A="BGIPSVUKG"
B=[
    [2,6],[4,7],[6,7]
]
print(solve(A,B))