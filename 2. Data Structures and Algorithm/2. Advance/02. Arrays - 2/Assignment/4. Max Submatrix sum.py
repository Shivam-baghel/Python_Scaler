""" 
Q4. Maximum Submatrix Sum

Given a row-wise and column-wise sorted matrix A of size N * M.
Return the maximum non-empty submatrix sum of this matrix.

Problem Constraints
1 <= N, M <= 1000
-109 <= A[i][j] <= 109

Input Format
The first argument is a 2D integer array A.

Output Format
Return a single integer that is the maximum non-empty submatrix sum of this matrix.

Example Input
Input 1:-
    -5 -4 -3
A = -1  2  3
     2  2  4
Input 2:-
    1 2 3
A = 4 5 6
    7 8 9

Example Output
Output 1:-
12
Output 2:-
45

Example Explanation
Expanation 1:-
The submatrix with max sum is 
-1 2 3
 2 2 4
 Sum is 12.
Explanation 2:-
The largest submatrix with max sum is 
1 2 3
4 5 6
7 8 9
The sum is 45.
"""

def maxSubmatrixSum( A):
    def prefix_matrix(A):
                n = len(A)
                m = len(A[0])

                for i in range(n):
                    for j in range(1,m):
                        A[i][j] = A[i][j-1] + A[i][j]
            
                for i in range(1,n):
                    for j in range(m):
                        A[i][j] = A[i-1][j] + A[i][j]
                return A
    
    A = prefix_matrix(A)
    # print(A)

    brr = len(A)-1
    brc = len(A[0])-1
    maxsum = A[brr][brc]

    for tlr in range(brr + 1):
        for tlc in range(brc + 1):
            sum = 0
            if tlr <= 0 and tlc <= 0:
                sum = A[brr][brc]
            elif tlr <= 0 and tlc > 0:
                sum = A[brr][brc] - A[brr][tlc-1]
            elif tlr > 0 and tlc <= 0:
                sum = A[brr][brc] - A[tlr-1][brc]
            else:
                sum = A[brr][brc] - A[brr][tlc-1] - A[tlr-1][brc] + A[tlr-1][tlc-1]

            maxsum = max(maxsum,sum)
        # print(maxsum)
    return maxsum