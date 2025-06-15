""" 
Q1. Subset

Given a set of distinct integers A, return all possible subsets.

NOTE:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The initial list is not necessarily sorted.


Problem Constraints

1 <= |A| <= 16
INTMIN <= A[i] <= INTMAX


Input Format
First and only argument of input contains a single integer array A.

Output Format
Return a vector of vectors denoting the answer.


Example Input

Input 1:
A = [1]

Input 2:
A = [1, 2, 3]


Example Output

Output 1:
[
    []
    [1]
]

Output 2:
[
 []
 [1]
 [1, 2]
 [1, 2, 3]
 [1, 3]
 [2]
 [2, 3]
 [3]
]


Example Explanation

Explanation 1:
 You can see that these are all possible subsets.
 
Explanation 2:
You can see that these are all possible subsets.

"""

ans = []
curr = []


def solve(i, n, A):
    global ans, curr
    if i == n:
        ans.append(sorted(curr.copy()))
        return
    # for every element we can either take it or skip it
    solve(i + 1, n, A)
    curr.append(A[i])
    solve(i + 1, n, A)
    curr.pop()


# @param A : list of integers
# @return a list of list of integers
def subsets(A):
    global ans, curr
    ans = []
    n = len(A)
    solve(0, n, A)
    return sorted(ans)
