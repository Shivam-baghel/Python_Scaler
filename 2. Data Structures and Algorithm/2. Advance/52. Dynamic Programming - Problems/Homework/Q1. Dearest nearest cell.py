""" 
Q1. Distance of nearest cell

Given a matrix of integers A of size N x M consisting of 0 or 1.
For each cell of the matrix find the distance of nearest 1 in the matrix.
Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.
Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.

NOTE: There is atleast one 1 is present in the matrix.


Problem Constraints
1 <= N, M <= 1000
0 <= A[i][j] <= 1

Input Format
The first argument given is the integer matrix A.

Output Format
Return the matrix B.

Example Input

Input 1:

 A = [
       [0, 0, 0, 1]
       [0, 0, 1, 1] 
       [0, 1, 1, 0]
     ]
Input 2:

 A = [
       [1, 0, 0]
       [0, 0, 0]
       [0, 0, 0]  
     ]


Example Output

Output 1:

 [ 
   [3, 2, 1, 0]
   [2, 1, 0, 0]
   [1, 0, 0, 1]   
 ]
Output 2:

 [
   [0, 1, 2]
   [1, 2, 3]
   [2, 3, 4] 
 ]


Example Explanation

Explanation 1:

 A[0][0], A[0][1], A[0][2] will be nearest to A[0][3].
 A[1][0], A[1][1] will be nearest to A[1][2].
 A[2][0] will be nearest to A[2][1] and A[2][3] will be nearest to A[2][2].
Explanation 2:

 There is only a single 1. Fill the distance from that 1.
"""

from collections import deque

# @param A : list of list of integers
# @return a list of list of integers


def nearestCell(grid):
    N, M = len(grid), len(grid[0])

    visited = [[False] * M for _ in range(N)]

    q = deque()

    for i in range(N):
        for j in range(M):
            # we are appending all the Ones intially in Queue
            if grid[i][j] == 1:
                visited[i][j] = True
                q.append((i, j, 0))
                grid[i][j] = 0  # make it zero

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while q:
        row, col, count = q.popleft()

        for i, j in directions:
            cr = row + i
            cc = col + j

            if (
                cr < 0
                or cc < 0
                or cr >= N
                or cc >= M
                or visited[cr][cc]
                or grid[cr][cc] != 0
            ):
                continue

            grid[cr][cc] = count + 1
            visited[cr][cc] = True
            q.append((cr, cc, count + 1))

    return grid
