""" 
Q1. Valid Path
There is a rectangle with left bottom as (0, 0) and right up as (x, y).
There are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.
Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.

Problem Constraints
0 <= x , y, R <= 100
1 <= N <= 1000
Center of each circle would lie within the grid

Input Format
1st argument given is an Integer x , denoted by A in input.
2nd argument given is an Integer y, denoted by B in input.
3rd argument given is an Integer N, number of circles, denoted by C in input.
4th argument given is an Integer R, radius of each circle, denoted by D in input.
5th argument given is an Array A of size N, denoted by E in input, where A[i] = x cordinate of ith circle
6th argument given is an Array B of size N, denoted by F in input, where B[i] = y cordinate of ith circle

Output Format
Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).

Example Input
Input 1:
 x = 2
 y = 3
 N = 1
 R = 1
 A = [2]
 B = [3]
Input 2:
 x = 1
 y = 1
 N = 1
 R = 1
 A = [1]
 B = [1]

Example Output
Output 1:
 NO
Output 2:
 NO

Example Explanation
Explanation 1:
 There is NO valid path in this case
Explanation 2:
 There is NO valid path in this case
"""


def dfs(x1, y1, x2, y2, visited):
    
    # check if x1 or y1 are out of bounds
    if (x1 < 0 or y1 < 0 or x1 >= len(visited) or y1 >= len(visited[0]) or visited[x1][y1]):
        return False
    
    # as we have visited this cell right now. make this true in visited array.
    visited[x1][y1] = True
    # if x1 and y1 are equal to x2 and y2 then change the value of the flag and return.
    if (x1 == x2 and y1 == y2):
        return True
    
    # visited all adjacent cells around the current cell.
    if dfs(x1 - 1, y1 - 1, x2, y2, visited):
        return True
    if dfs(x1 - 1, y1 + 1, x2, y2, visited):
        return True
    if dfs(x1 + 1, y1 - 1, x2, y2, visited):
        return True
    if dfs(x1 + 1, y1 + 1, x2, y2, visited):
        return True
    if dfs(x1 - 1, y1, x2, y2, visited):
        return True
    if dfs(x1 + 1, y1, x2, y2, visited):
        return True
    if dfs(x1, y1 - 1, x2, y2, visited):
        return True
    if dfs(x1, y1 + 1, x2, y2, visited):
        return True

    return False


    
def validPath(A, B, C, D, E, F):
    x = A
    y = B
    numOfCenters = C
    radius = D
    arrOfx = E
    arrOfy = F

    # for dimensions of visited array.
    # n represents the vertical part
    n = y+1
    # m represents the horizontal part.
    m = x+1
    # To count the no. of islands.
    c = 0
    
    # create a visited array.
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            
            for k in range(numOfCenters):
                dist = (i - E[k]) * (i - E[k]) + (j - F[k]) * (j - F[k]);
                if (dist <= radius * radius):
                    visited[i][j] = True
                    break
                    
    # check if x or y are out of bounds or not.
    if x < 0 or x >= len(visited) or y < 0 or y >= len(visited[0]):
        return 'NO'
    # check if source cell or destination cell are reachable or not
    if visited[x][y] == True or visited[0][0] == True:
        return 'NO'
    # if source cell or destination cell are reachable then try to find out the path between source and destination cell. If True return yes else no
    
    if dfs(0, 0, x, y, visited):
        return 'YES'
    else:
        return 'NO'
    
x = 2
y = 3
N = 1
R = 1
A = [2]
B = [3]
print(validPath(x,y,N,R,A,B))
