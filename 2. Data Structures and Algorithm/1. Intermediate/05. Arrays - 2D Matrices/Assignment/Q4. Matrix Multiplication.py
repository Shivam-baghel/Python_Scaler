""" 
Q4. Matrix Multiplication

You are given two integer matrices A(having M X N size) and B(having N X P). You have to multiply matrix A with B and return the resultant matrix. (i.e. return the matrix AB).

Matrix Multiplication 


Problem Constraints
1 <= M, N, P <= 100

-100 <= A[i][j], B[i][j] <= 100



Input Format
The first argument given is the 2-D integer matrix A.
The second argument given is the 2-D integer matrix B.



Output Format
Return a 2D integer matrix denoting AB.



Example Input
Input 1:

A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
Input 2:

A = [[1, 1]]
B = [[2],
     [3]]


Example Output
Output 1:

 [[19, 22],
  [43, 50]]
Output 2:

 [[5]]


Example Explanation
Explanation 1:

 image
Explanation 2:

 [[1, 1]].[[2], [3]] = [[1 * 2 + 1 * 3]] = [[5]]
"""

def matrix_multiplication( A, B):
    rowA = len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])


    rows, cols = (rowA, colB) # p x q
    C = [[0 for i in range(cols)] for j in range(rows)] # gen C


    for i in range(rowA):
        for j in range(colB):
            for k in range(rowB):
                row = A[i][k]
                col = B[k][j]
                C[i][j] += row * col

    return(C)