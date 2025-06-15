""" 
Q4. Construct Roads
Solved
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description

A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads such that the new country formed remains bipartite country.

Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v) that belongs to the country, u and v belong to different sets. Also, there should be no multiple roads between two cities and no self loops.

Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.

NOTE: All cities can be visited from any city.



Problem Constraints

1 <= A <= 105

1 <= B[i][0], B[i][1] <= N



Input Format

First argument is an integer A denoting the number of cities, N.

Second argument is a 2D array B of size (N-1) x 2 denoting the initial roads i.e. there is a road between cities B[i][0] and B[1][1] .



Output Format

Return an integer denoting the maximum number of roads king can construct.



Example Input

Input 1:

 A = 3
 B = [
       [1, 2]
       [1, 3]
     ]
Input 2:

 A = 5
 B = [
       [1, 3]
       [1, 4]
       [3, 2]
       [3, 5]
     ]


Example Output

Output 1:

 0
Output 2:

 2


Example Explanation

Explanation 1:

 We can't construct any new roads such that the country remains bipartite.
Explanation 2:

 We can add two roads between cities (4, 2) and (4, 5).
"""

from collections import deque


# @param A : integer
# @param B : list of list of integers
# @return an integer


def constructRoads(A, B):
    mod = 10**9 + 7
    """
    A few more lines of code to get you from Q3. Check Bipartite Graph to Q4. Construct Roads
    4 Functions 
    graphBuilder -> builds our flattened graph

    isBiPartite. -> checks bipartite condition with queue.

    colorUpdate. -> generates the updated color/visited array after done with traversal.

    Solve(A,B,color)  -> Use dictionary to get counts of each state/color and return all combinations possible . 
                        This function also handles return 0 incase graph isn't bipartite
    """

    def biparte(node, mat):
        edge = len(mat)
        # step 1 construct adjacency list
        g = [[] for i in range(node + 1)]
        for i in range(edge):
            # ith edge : u[i] --- v[i]
            a = mat[i][0]
            b = mat[i][1]
            g[a].append(b)
            # make the below line comment to make code work for directed graph
            g[b].append(a)

        # step 2

        # create a queue
        queue = deque()
        # create a color array. 0 = no color, 1 = green color, 2 = blue color.
        color = [0] * (node + 1)

        for i in range(1, node + 1):

            if color[i] == 0:

                color[i] = 1
                queue.append(i)

                while len(queue) > 0:

                    u = queue.popleft()
                    # iterate on adj nodes of u
                    for j in range(len(g[u])):
                        # all the nodes connected to g[u]
                        v = g[u][j]

                        if color[v] == 0:
                            color[v] = 3 - color[u]
                            queue.append(v)
                        elif color[u] == color[v]:
                            return 0

        # step 3
        cg = 0
        cb = 0
        for i in range(1, node + 1):
            if color[i] == 1:
                cg += 1
            else:
                cb += 1

        return cg * cb - edge

    return biparte(A, B) % mod
