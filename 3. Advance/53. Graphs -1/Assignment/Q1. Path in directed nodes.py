""" 
Q1. Path in Directed Graph
Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2such that there is a edge directed from node
B[i][0] to node B[i][1].
Find whether a path exists from node 1 to node A.
Return 1 if path exists else return 0.

NOTE:
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.

Problem Constraints
2 <= A <= 105
1 <= M <= min(200000,A*(A-1))
1 <= B[i][0], B[i][1] <= A

Input Format
The first argument given is an integer A representing the number of nodes in the graph.
The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Output Format
Return 1 if path exists between node 1 to node A else return 0.

Example Input
Input 1:

 A = 5
 B = [  [1, 2] 
        [4, 1] 
        [2, 4] 
        [3, 4] 
        [5, 2] 
        [1, 3] ]
Input 2:

 A = 5
 B = [  [1, 2]
        [2, 3] 
        [3, 4] 
        [4, 5] ]
        
Example Output
Output 1:
 0
Output 2:
 1

Example Explanation
Explanation 1:
 The given doens't contain any path from node 1 to node 5 so we will return 0.
Explanation 2:
 Path from node1 to node 5 is ( 1 -> 2 -> 3 -> 4 -> 5 ) so we will return 1.
"""
from collections import deque 

def BreadthFirstSearch(node,edge,u,v,source,destination):
    
    g = [[] for i in range(node+1)]
    for i in range(edge):
        # ith edge : u[i] --- v[i]
        a = u[i]
        b = v[i]
        g[a].append(b)
        # make the below line comment to make code work for directed graph
        # g[b].append(a)
    
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