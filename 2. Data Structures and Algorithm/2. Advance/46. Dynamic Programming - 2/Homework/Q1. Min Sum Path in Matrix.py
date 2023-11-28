""" 
Q1. Min Sum Path in Matrix
Given a M x N grid A of integers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Return the minimum sum of the path.
NOTE: You can only move either down or right at any point in time.

Problem Constraints
1 <= M, N <= 2000
-1000 <= A[i][j] <= 1000

Input Format
First and only argument is a 2-D grid A.

Output Format
Return an integer denoting the minimum sum of the path.

Example Input
Input 1:
 A = [
       [1, 3, 2]
       [4, 3, 1]
       [5, 6, 1]
     ]
Input 2:
 A = [
       [1, -3, 2]
       [2, 5, 10]
       [5, -5, 1]
     ]

Example Output
Output 1:
 8
Output 2:
 -1

Example Explanation
Explanation 1:
 The path will be: 1 -> 3 -> 2 -> 1 -> 1.
Input 2:
 The path will be: 1 -> -3 -> 5 -> -5 -> 1.
 
"""

def uniquePathsWithObstacles(A):
  n = len(A)
  m = len(A[0])

  # create a dp matrix
  dp=[]
  rows, cols=n,m
  for i in range(rows):
    col = []
    for j in range(cols):
      col.append(None)
    dp.append(col)
  # print(arr)


  def minSumPath(i,j,A):
    # checking if i or j have  become less than 0
    if i<0 or j<0 : 
      return float('inf')
    # checking if the current cell is blocked or not
    # if A[i][j] == 1:
    #       return 0
    # checking if we have reached top left cell of the matrix
    if i == 0 and j == 0 :
      return A[i][j]
    
    # if the current cell value in dp matrix is -1 i.e cell is not reached before.
    if dp[i][j] == None:
          dp[i][j] = min(minSumPath(i-1,j,A),minSumPath(i,j-1,A)) +A[i][j]
    
    # return the stored value of the current cell in dp matrix.
    return dp[i][j]

  return minSumPath(n-1,m-1,A)


if __name__ == "__main__":
  
  A = [
        [1, 3, 2],
        [4, 3, 1],
        [5, 6, 1],
      ] 

  print(uniquePathsWithObstacles(A))