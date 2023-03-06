""" 
Q3. Number of islands II
Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island.
From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a side with (i, j) and value in that cell is 1.
More formally, from any cell (i, j) if A[i][j] = 1 you can visit:
(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
Return the number of islands.

Note:
Rows are numbered from top to bottom and columns are numbered from left to right.
Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.

Input Format
The only argument given is the integer matrix A.

Output Format
Return the number of islands.

Constraints
1 <= N, M <= 100
0 <= A[i] <= 1

For Example
Input 1:
    A = [   [0, 1, 0]
            [0, 0, 1]
            [1, 0, 0]   ]
Output 1:
    3

Input 2:
      A = [ [1, 1, 0, 0, 0]
            [1, 1, 0, 0, 0]
            [0, 0, 1, 0, 0]
            [0, 0, 0, 1, 1]    ]
Output 2:
    3
"""

def dfs(mat,i,j):
    n = len(mat)
    m = len(mat[0])
    if i<0 or j<0 or i>=n or j>=m or mat[i][j] == 0:
        return
    
    # Make this particular cell equal to 0
    mat[i][j] = 0
    
    # call adj cells
    # if adj cells are also 1 then making them 0
    dfs(mat,i-1,j)
    dfs(mat,i+1,j)
    dfs(mat,i,j-1)
    dfs(mat,i,j+1)
    
def islands(mat):
    # rows in matrix
    n = len(mat)
    # columns in matrix
    m = len(mat[0])
    # To count the no. of islands.
    c = 0
    #iterate over each cell to check for islands
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                
                # for counting the islands
                c = c+1
                # making the entire island disappear by making cell equal to 0
                dfs(mat,i,j)
    
    return c

A = [ 
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
    ]

print(islands(A))