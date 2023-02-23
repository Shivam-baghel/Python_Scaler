"""
Q2. Poisonous Graph
You are given an undirected unweighted graph consisting of A vertices and M edges given in a form of 2D Matrix B of size M x 2 where (B[i][0], B][i][1]) denotes two nodes connected by an edge.

You have to write a number on each vertex of the graph. Each number should be 1, 2 or 3. The graph becomes Poisonous if for each edge the sum of numbers on vertices connected by this edge is odd.

Calculate the number of possible ways to write numbers 1, 2 or 3 on vertices so the graph becomes poisonous. Since this number may be large, return it modulo 998244353.

NOTE:
Note that you have to write exactly one number on each vertex.
The graph does not have any self-loops or multiple edges.
Nodes are labelled from 1 to A.

Problem Constraints
1 <= A <= 3*105
0 <= M <= 3*105
1 <= B[i][0], B[i][1] <= A
B[i][0] != B[i][1]

Input Format
First argument is an integer A denoting the number of nodes.
Second argument is an 2D Matrix B of size M x 2 denoting the M edges.

Output Format
Return one integer denoting the number of possible ways to write numbers 1, 2 or 3 on the vertices of given graph so it becomes Poisonous . Since answer may be large, print it modulo 998244353.

Example Input
Input 1:
 A = 2
 B = [  [1, 2]
     ]
Input 2:
 A = 4
 B = [  [1, 2]
        [1, 3]
        [1, 4]
        [2, 3]
        [2, 4]
        [3, 4]
    ]

Example Output
Output 1:
 4
Output 2:
 0

Example Explanation
Explanation 1:
 There are 4 ways to make the graph poisonous. i.e, writing number on node 1 and 2 as,
    [1, 2] , [3, 2], [2, 1] or [2, 3] repsectively.
Explanation 2:
 There is no way to make the graph poisonous.
"""
from collections import deque

def poisonousGraph(vertice,edgeMat):
    mod = 998244353
    # get total no of edges
    edges = len(edgeMat)
    
    # create the adjanecy list
    adj = [[] for _ in range(vertice+1)]
    # fill up the adjanency list
    for i in range(edges):
        # ith edge : u[i] --- v[i]
        a = edgeMat[i][0]
        b = edgeMat[i][1]
        
        adj[a].append(b)
        # make the below line comment to make code work for directed graph
        adj[b].append(a)
    
    # create a queue
    queue = deque()
    # create even and odd sets
    evenSet = set()
    oddSet = set()
    
    # color list filled with 0
        # 0 represents no color
        # 1 represents green color or in this case odd
        # 2 represents blue color or in this case even
    color = [0]*(vertice+1)
    
    for i in range(vertice+1):
        if color[i] == 0:
            color[i] = 1    # give any color 1 or 2 
            # push it into the queue and the respective set.
            oddSet.add(i)
            queue.append(i)
            
            # perform operations untill queue becomes empty.
            while len(queue)>0:
                u = queue.popleft()
                # iterate on u
                for j in range(len(adj[u])):
                    v = adj[u][j]
                    # if color of v is not assigned
                    if color[v] == 0:
                        color[v] = 3-color[u]
                        queue.append(v)
                        if (3-color[u])% 2 == 0:
                            evenSet.add(v)
                        else:
                            oddSet.add(v)
                    elif color[v] == color[u]:
                        return 0
    
    # step 3 to calculate no of ways to make graph poisonous 
    # x represents even
    x = len(evenSet)
    # y represents odd
    y = len(oddSet)
    ans = ((2**x)+(2**y))%mod
    for i in range(vertice):
        ans = ans*ans
        
    return ans



# Input 1:
A = 2
B = [  [1, 2]
    ]
# Input 2:
# A = 4
# B = [  [1, 2],
#     [1, 3],
#     [1, 4],
#     [2, 3],
#     [2, 4],
#     [3, 4]
# ]

print(poisonousGraph(A,B))