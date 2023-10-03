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

def solve( A, B):
    pfList = []                 #Empty Prefix Array

    n = len(A)                  #Rows
    m = len(A[0])               #columns
                                
    #Creating 0 matrix
    for i in range(n):          
        pfList.append([0]*m)

    pfList[0][0] = A[0][0]      #First Element will remain same    


    #Sum rowwise in the matrix
    for i in range(1,m):    
        pfList[0][i] = A[0][i] + pfList[0][i-1]
    
    #Sum column wise in the matrix
    for i in range(1,n):
        pfList[i][0] = pfList[i-1][0] + A[i][0]

    #Full Prefix array creating
    for i in range(1,n):
        for j in range(1,m):
            pfList[i][j] = A[i][j] + pfList[i-1][j] + pfList[i][j-1] - pfList[i-1][j-1]
    
    ans = -1000000
    curSum = 0
    for c in range(B-1,n):
        for d in range(B-1,m):
            a,b = c-(B-1), d-(B-1)      # a,b = Top Left corners and c,d = Button righ corners
            if a == 0 and b == 0:
                curSum = pfList[c][d]
            elif a == 0 and b != 0:
                curSum = pfList[c][d] - pfList[c][b-1]
            elif b == 0 and a != 0:
                curSum = pfList[c][d] - pfList[a-1][d]
            else:
                curSum = pfList[c][d] - pfList[c][b-1] - pfList[a-1][d] + pfList[a-1][b-1]
            ans = max(ans,curSum)
    return ans
# Please like the post if it is helpful for you