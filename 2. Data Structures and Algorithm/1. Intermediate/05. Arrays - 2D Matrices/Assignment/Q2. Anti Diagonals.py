""" 
Q2. Anti Diagonals

Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.

Problem Constraints
1<= N <= 1000
1<= A[i][j] <= 1e9

Input Format
Only argument is a 2D array A of size N * N.

Output Format
Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
The vacant spaces in the grid should be assigned to 0.

Example Input
Input 1:
1 2 3
4 5 6
7 8 9
Input 2:

1 2
3 4

Example Output
Output 1:
1 0 0
2 4 0
3 5 7
6 8 0
9 0 0
Output 2:

1 0
2 3
4 0


Example Explanation
For input 1:
The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 5, 7 ], the rest spaces shoud be filled with 0 making the row as [3, 5, 7].
The fourth anti diagonal of the matrix is [6, 8 ], the rest spaces shoud be filled with 0 making the row as [6, 8, 0].
The fifth anti diagonal of the matrix is [9 ], the rest spaces shoud be filled with 0 making the row as [9, 0, 0].
For input 2:

The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 0, 0 ], the rest spaces shoud be filled with 0 making the row as [3, 0, 0].
"""


def diagonal(A):
    lengthOfRow = len(A)
    res = []
    for i in range((2 * lengthOfRow) - 1):
        res.append([0] * lengthOfRow)

    for j in range(0, lengthOfRow):
        x = 0
        y = j
        while x < lengthOfRow and y >= 0:
            res[x + y][x] = A[x][y]
            x += 1
            y -= 1

    for i in range(1, lengthOfRow):
        x = i
        y = lengthOfRow - 1
        l = 0
        while x < lengthOfRow and y >= 0:
            res[x + y][l] = A[x][y]
            x += 1
            y -= 1
            l += 1

    return res


if __name__ == '__main__':
    a = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    print(diagonal(a))