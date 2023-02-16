

from collections import deque

def rottenOranges(mat):
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
            if x+1 >= 0 and mat[x+1][y] == 1:
                mat[x+1][y] = 2
                queue.append([x+1,y])
            if y-1 >= 0 and mat[x][y-1] == 1:
                mat[x][y-1] = 2
                queue.append([x,y-1])
            if y+1 >= 0 and mat[x][y+1] == 1:
                mat[x][y+1] = 2
                queue.append([x,y+1])
    
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                return -1
    
    return l-1