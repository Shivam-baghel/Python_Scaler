"""
Q3. Construction Cost
Given a graph with A nodes and C weighted edges. Cost of constructing the graph is the sum of weights of all the edges in the graph.

Find the minimum cost of constructing the graph by selecting some given edges such that we can reach every other node from the 1st node.

NOTE: Return the answer modulo 109+7 as the answer can be large.

Problem Constraints
1 <= A <= 100000
0 <= C <= 100000
1 <= B[i][0], B[i][1] <= N
1 <= B[i][2] <= 109

Input Format
First argument is an integer A.
Second argument is a 2-D integer array B of size C*3 denoting edges. B[i][0] and B[i][1] are connected by ith edge with weight B[i][2]

Output Format
Return an integer denoting the minimum construction cost.

Example Input
Input 1:
A = 3
B = [   [1, 2, 14]
        [2, 3, 7]
        [3, 1, 2]   ]
Input 2:
A = 3
B = [   [1, 2, 20]
        [2, 3, 17]  ]


Example Output
Output 1:
9
Output 2:
37

Example Explanation

Explanation 1:
We can take only two edges (2 -> 3 and 3 -> 1) to construct the graph. 
we can reach the 1st node from 2nd and 3rd node using only these two edges.
So, the total cost of costruction is 9.

Explanation 2:
We have to take both the given edges so that we can reach the 1st node from 2nd and 3rd node.
"""

def find(x,component):
    if x == component[x]:
        return x
    component[x] = find(component[x],component)
    return component[x]

def Construction(node, mat):
    # sort the mat based on wieght
    def algo(e):
        return e[2]
    mat.sort(key = algo)
    
    # create component list
    comp = [0]*(node+1)
    
    # fill component list with their values
    for i in range(node+1):
        comp[i] = i
    
    # get min weight
    totalCost = 0
    for i in range(len(mat)):
        d = mat[i]
        w = d[2]
        u = d[0]
        v = d[1]
        
        # find super component for u and v
        cu = find(u,comp)
        cv = find(v,comp)
        
        if cu != cv:
            totalCost += w
            comp[max(cu,cv)] = comp[min(cu,cv)]
            
    return totalCost