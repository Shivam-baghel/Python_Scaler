""" 
Q2. Commutable Islands

There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.
We need to find bridges with minimal cost such that all islands are connected.
It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.

Problem Constraints
1 <= A, M <= 6*104
1 <= B[i][0], B[i][1] <= A
1 <= B[i][2] <= 103

Input Format
The first argument contains an integer, A, representing the number of islands.
The second argument contains an 2-d integer matrix, B, of size M x 3 where Island B[i][0] and B[i][1] are connected using a bridge of cost B[i][2].

Output Format
Return an integer representing the minimal cost required.

Example Input
Input 1:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 4]
        [1, 4, 3]
        [4, 3, 2]
        [1, 3, 10]  ]
Input 2:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 2]
        [3, 4, 4]
        [1, 4, 3]   ]


Example Output
Output 1:
 6
Output 2:
 6

Example Explanation
Explanation 1:
 We can choose bridges (1, 2, 1), (1, 4, 3) and (4, 3, 2), where the total cost incurred will be (1 + 3 + 2) = 6.
Explanation 2:
 We can choose bridges (1, 2, 1), (2, 3, 2) and (1, 4, 3), where the total cost incurred will be (1 + 2 + 3) = 6.
"""
def find(x,component):
    if x == component[x]:
        return x
    component[x] = find(component[x],component)
    return component[x]

def CommutableIslands(node, mat):
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
    ans = 0
    for i in range(len(mat)):
        d = mat[i]
        w = d[2]
        u = d[0]
        v = d[1]
        
        # find super component for u and v
        cu = find(u,comp)
        cv = find(v,comp)
        
        if cu != cv:
            ans += w
            comp[max(cu,cv)] = comp[min(cu,cv)]
            
    return ans

A = 4
B = [  [1, 2, 1],
    [2, 3, 4],
    [1, 4, 3],
    [4, 3, 2],
    [1, 3, 10]  ]

print(CommutableIslands(A,B))