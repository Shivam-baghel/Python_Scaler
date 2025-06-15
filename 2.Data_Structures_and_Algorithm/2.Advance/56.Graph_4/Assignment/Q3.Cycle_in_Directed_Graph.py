""" 
Q3. Cycle in Directed Graph
Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast two nodes.
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
Return 1 if cycle is present else return 0.

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
 1
Output 2:
 0


Example Explanation
Explanation 1:
 The given graph contain cycle 1 -> 3 -> 4 -> 1 or the cycle 1 -> 2 -> 4 -> 1
Explanation 2:
 The given graph doesn't contain any cycle.
"""

import sys 
sys.setrecursionlimit(10**6)

# @param A : integer
# @param B : list of list of integers
# @return an integer

def dfs(node,visited,Path_visited,adj):
    if not node:
        return 

    visited[node]      = True 
    Path_visited[node] = True


    for child in adj[node]:
        if not visited[child]:
            if dfs(child,visited,Path_visited,adj):
                return True 
        else:
            if visited[child] and Path_visited[child]:  #path is already visited  from different path 
                return True 


    Path_visited[node] = False     # while coming back to root , make it unvisited -> indicates visited from cur run 

    return False




def cycleInDirGraph(self, A, B):
    N = A
    visited = [False] * (N+1)
    Path_visited = [False] * (N+1)       # we are using this path array to indicate in current run these nodes - visited 
    adj     = [[] for _ in range(N+1)]
    for i in range(len(B)):
        u = B[i][0]
        v = B[i][1]
        adj[u].append(v)


    for node in range(1,N+1):
        if not visited[node]:
            if dfs(node,visited,Path_visited,adj):
                return 1 

    return 0