""" 
given a undirected graph and source node and destination node. check if you  can travel from source node to destination node.
"""
from collections import deque
""" My idea: 
    make a list of list integers meaning the index of list of integers in the list is having the direct connection as index value as source node and integer in the particular list as destination nodes.
    
    make a visited array of same length as the no.of nodes containing false. meaning none of the nodes have been visited yet.
    
    create a queue and append the source node and make visited array[source] == True meaning that particular index is visited or that node is visited.
    check in list named g that source node is having any connecting nodes. and go through each of those connecting nodes and check if they have any connecting nodes repeat this untill all the connecting nodes gets over.
    mark true for all the nodes that you were able to visit in visited array.
    
    return the asked visited node from visited array.
"""
def BreadthFirstSearch(node,edge,u,v,source,destination):
    
    g = [[] for i in range(node+1)]
    for i in range(edge):
        # ith edge : u[i] --- v[i]
        a = u[i]
        b = v[i]
        g[a].append(b)
        # make the below line comment to make code work for directed graph
        g[b].append(a)
    
    # step 2 : apply bfs 
    visited = [False]*(node+1)
    # create queue
    queue = deque()
    queue.append(source)
    visited[source] = True
    
    while len(queue) > 0:
        x = queue[0]    # or you can write queue.popleft()
        queue.popleft()
        
        for j in range(len(g[x])):
            y = g[x][j]
            # in visited array if index is false make it true and append it to queue.
            if visited[y] == False:
                visited[y] = True
                queue.append(y)
    # return distination index of the visited array.
    return visited[destination]

def main():

    A = 5
    B = [  [1, 2], 
        [4, 1],
        [2, 4],
        [3, 4],
        [5, 2],
        [1, 3] ]
    u = []
    for i in range(len(B)):
        u.append(B[i][0])
    v = []
    for i in range(len(B)):
        v.append(B[i][1])
    print(BreadthFirstSearch(A,len(B),u,v,1,A))
    
if __name__ == "__main__":
    main()