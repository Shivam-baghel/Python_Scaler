""" 

Q1. Unique Paths in a Grid
Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).
Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Problem Constraints
1 <= n, m <= 100
A[i][j] = 0 or 1

Input Format
Firts and only argument A is a 2D array of size n * m.

Output Format
Return an integer denoting the number of unique paths from (1, 1) to (n, m).

Example Input
Input 1:
 A = [
        [0, 0, 0]
        [0, 1, 0]
        [0, 0, 0]
     ]
Input 2:
 A = [
        [0, 0, 0]
        [1, 1, 1]
        [0, 0, 0]
     ]

Example Output
Output 1:
 2
Output 2:
 0


Example Explanation
Explanation 1:
 Possible paths to reach (n, m): {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)} and {(1 ,1), (2, 1), (3, 1), (3, 2), (3, 3)}  
 So, the total number of unique paths is 2. 
Explanation 2:
 It is not possible to reach (n, m) from (1, 1). So, ans is 0.
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
                  col.append(-1)
            dp.append(col)
      # print(arr)


      def ways(i,j,A):
            # checking if i or j have  become less than 0
            if i<0 or j<0 : 
                  return 0
            # checking if the current cell is blocked or not
            if A[i][j] == 1:
                  return 0
            # checking if we have reached top left cell of the matrix
            if i == 0 and j == 0 :
                  return 1
            
            # if the current cell value in dp matrix is -1 i.e cell is not reached before.
            if dp[i][j] == -1:
                  dp[i][j] = ways(i-1,j,A)+ways(i,j-1,A)
            
            # return the stored value of the current cell in dp matrix.
            return dp[i][j]

      return ways(n-1,m-1,A)

def main():
      A = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
      ]

      print(uniquePathsWithObstacles(A))

if __name__ == "__main__":
      main()

