""" 
Q2. Maximum Sum Square SubMatrix

Given a 2D integer matrix A of size N x N, find a B x B submatrix where B<= N and B>= 1, such that the sum of all the elements in the submatrix is maximum.

Problem Constraints
1 <= N <= 103.
1 <= B <= N
-102 <= A[i][j] <= 102.

Input Format
First arguement is an 2D integer matrix A.
Second argument is an integer B.

Output Format
Return a single integer denoting the maximum sum of submatrix of size B x B.

Example Input
Input 1:

 A = [
        [1, 1, 1, 1, 1]
        [2, 2, 2, 2, 2]
        [3, 8, 6, 7, 3]
        [4, 4, 4, 4, 4]
        [5, 5, 5, 5, 5]
     ]
 B = 3
Input 2:

 A = [
        [2, 2]
        [2, 2]
    ]
 B = 2


Example Output
Output 1:
 48
Output 2:
 8

Example Explanation
Explanation 1:

    Maximum sum 3 x 3 matrix is
    8 6 7
    4 4 4
    5 5 5
    Sum = 48
Explanation 2:

 Maximum sum 2 x 2 matrix is
  2 2
  2 2
  Sum = 8
"""


def solve(A, B):
    pf_list = []  # Empty Prefix Array

    n = len(A)  # Rows
    m = len(A[0])  # columns

    # Creating 0 matrix
    for i in range(n):
        pf_list.append([0] * m)

    pf_list[0][0] = A[0][0]  # First Element will remain same

    # Sum rowwise in the matrix
    for i in range(1, m):
        pf_list[0][i] = A[0][i] + pf_list[0][i - 1]

    # Sum column wise in the matrix
    for i in range(1, n):
        pf_list[i][0] = pf_list[i - 1][0] + A[i][0]

    # Full Prefix array creating
    for i in range(1, n):
        for j in range(1, m):
            pf_list[i][j] = A[i][j] + pf_list[i - 1][j] + pf_list[i][j - 1] - pf_list[i - 1][j - 1]

    ans = -1000000
    cur_sum = 0
    for c in range(B - 1, n):
        for d in range(B - 1, m):
            a, b = c - (B - 1), d - (B - 1)  # a,b = Top Left corners and c,d = Button righ corners
            if a == 0 and b == 0:
                cur_sum = pf_list[c][d]
            elif a == 0 and b != 0:
                cur_sum = pf_list[c][d] - pf_list[c][b - 1]
            elif b == 0 and a != 0:
                cur_sum = pf_list[c][d] - pf_list[a - 1][d]
            else:
                cur_sum = pf_list[c][d] - pf_list[c][b - 1] - pf_list[a - 1][d] + pf_list[a - 1][b - 1]
            ans = max(ans, cur_sum)
    return ans
# Please like the post if it is helpful for you
