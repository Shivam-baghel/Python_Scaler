""" 
Q2. Poisonous Graph
Solved
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description

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

def poisonousGraph( A, B):
    mod = 998244353
    maxn = 600005  # Maximum number of nodes (twice the given constraint)
    
    def pre():
        dp = [0] * maxn
        dp[0] = 1
        for i in range(1, maxn):
            dp[i] = (2 * dp[i - 1]) % mod
        return dp
    
    def bfs(s, a, b):
        visited[s] = 1
        a[0] += 1
        queue = [s]
        while queue:
            temp = queue.pop(0)
            for v in adj[temp]:
                if not visited[v]:
                    visited[v] = 1
                    color[v] = 1 - color[temp]
                    if color[v] == 0:
                        a[0] += 1
                    else:
                        b[0] += 1
                    queue.append(v)
                elif color[v] == color[temp]:
                    return False
        return True
    
    adj = [[] for _ in range(maxn)]
    visited = [0] * maxn
    color = [0] * maxn
    
    for edge in B:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])
        
    ans = 1
    dp = pre()
    
    for i in range(1, A + 1):
        if not visited[i]:
            a = [0]  # Counter for color 0
            b = [0]  # Counter for color 1
            if not bfs(i, a, b):
                return 0
            result = (dp[a[0]] + dp[b[0]]) % mod
            ans = (ans * result) % mod
            
    return ans