""" 
Q1. Rotten Oranges
Given a matrix of integers A of size N x M consisting of 0, 1 or 2.
Each cell can have three values:
The value 0 representing an empty cell.
The value 1 representing a fresh orange.
The value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.

Problem Constraints
1 <= N, M <= 1000
0 <= A[i][j] <= 2

Input Format
The first argument given is the integer matrix A.

Output Format
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1 instead.

Example Input
Input 1:
A = [   [2, 1, 1]
        [1, 1, 0]
        [0, 1, 1]   ]
Input 2:
A = [   [2, 1, 1]
        [0, 1, 1]
        [1, 0, 1]   ]

Example Output
Output 1:
 4
Output 2:
 -1

Example Explanation
Explanation 1:
 Max of 4 using (0,0) , (0,1) , (1,1) , (1,2) , (2,2)
Explanation 2:
 Task is impossible

"""
from collections import deque

def rottenOranges(A):

    mat = A
    queue = deque()
    pair = []
    N = len(mat)
    M = len(mat[0])
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 2:
                queue.append([i,j])
                
    l = 0   # before pushing an orange mark rotten
    
    while(len(queue) > 0):
        n = len(queue)
        l = l+1
        for i in range(n):
            # we delete all nodes at a level
            # calculating no. of level are there, ans = level-1
            
            element = queue.popleft()
            x = element[0]
            y = element[1]
            # adj nodes of x,y = (x-1,y),(x+1,y),(x,y-1),(x,y+1)
            
            if x-1 >= 0 and mat[x-1][y] == 1:
                mat[x-1][y] = 2
                queue.append([x-1,y])
            if x+1 < N and mat[x+1][y] == 1:
                mat[x+1][y] = 2
                queue.append([x+1,y])
            if y-1 >= 0 and mat[x][y-1] == 1:
                mat[x][y-1] = 2
                queue.append([x,y-1])
            if y+1 < M and mat[x][y+1] == 1:
                mat[x][y+1] = 2
                queue.append([x,y+1])
        
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                return -1
    
    return l-1


A = [   [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]   ]

print(rottenOranges(A))