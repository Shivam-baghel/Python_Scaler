""" 
Q1. Maximum Sum Submatrix

Given a N * M 2D matrix A. Find the maximum sum sub-matrix from the matrix A. Return the Sum.

Problem Constraints
1 <= N, M <= 300
-104 <= A[i][j] <= 104

Input Format
The first argument is a 2D Integer array A.

Output Format
Return the sum of the maximum sum sub-matrix from matrix A.

Example Input
Input 1:-
    -6 -6
   -29 -8
A =  3 -8
   -15  2
    25 25
    20 -5
Input 2:-
A = -17 -2
     20 10

Example Output
Output 1:-
65
Output 2:-
30


Example Explanation
Explanation 1:-
The submatrix 
25 25
20 -5
has the highest submatrix sum 65.
Explanation 2:-
The submatrix 
20 10
has the highest sub matrix sum 30.
"""


def max_submatrix_sum(A):
    rows = len(A)
    cols = len(A[0])

    def kadane(arr):
        max_sum = float('-inf')
        cur_sum = 0
        for i in range(len(arr)):
            cur_sum += arr[i]

            max_sum = max(max_sum, cur_sum)

            if cur_sum < 0:
                cur_sum = 0

        return max_sum

    ans = float('-inf')
    for k in range(cols):
        arr = [0] * rows
        for j in range(k, cols):
            for i in range(rows):
                arr[i] = A[i][j] + arr[i]

            cur_sum = kadane(arr)
            ans = max(ans, cur_sum)

    return ans
