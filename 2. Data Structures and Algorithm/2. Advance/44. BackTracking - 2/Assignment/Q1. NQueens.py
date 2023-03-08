""" 
Q1. NQueens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer A, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
The final list should be generated in such a way that the indices of the queens in each list should be in reverse lexicographical order.

Problem Constraints
1 <= A <= 10

Input Format
First argument is an integer n denoting the size of chessboard

Output Format
Return an array consisting of all distinct solutions in which each element is a 2d char array representing a unique solution.

Example Input
Input 1:
A = 4
Input 2:
A = 1

Example Output
Output 1:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Output 1:
[
 [Q]
]


Example Explanation
Explanation 1:
There exist only two distinct solutions to the 4-queens puzzle:
Explanation 1:
There exist only one distinct solutions to the 1-queens puzzle:
"""
global ans 
ans = []

def valid(arr,row,col):
  """this function will validate. if cell is the valid cell to place a queen.

  Args:
      arr (list): 2D list.
      row (int): cell row no.
      col (int): cell column no.

  Returns:
      Boolean: True or False
  """
  #iterate on above columns
  for i in range(row):
    if arr[i][col]== 1:
      return False
  
  # checking on left diagonal
  i = row-1
  j = col-1
  while i>=0 and j>=0:
    if arr[i][j]==1:
      return False
    i-=1
    j-=1
  
  # checking on right diagonal
  i = row-1
  j = col+1
  while i>=0 and j<len(arr):
    if arr[i][j]==1:
      return False
    i-=1
    j+=1
  
  # returning True if there is no queen in either of the above checked direction.
  return True

def add_solution(arr):
  curr_list = []
  for row in range(len(arr)):
    sol = ""
    for col in range(len(arr)):
      val = arr[row][col]
      if val == 0:
        sol+='.'
      else:
        sol+="Q"
    curr_list.append(sol)
    
  ans.append(curr_list)
  return



# here curr_pos represent the row 
def NQueens(arr,length,curr_pos):
  # if curren position is equal to length of the 2D list
  # it means you covered entire 2D list, now add the list to the ans list
  if curr_pos == length:
    add_solution(arr)
    return
  
  # At ith row choice 
  for col in range(0,length):
    
    # we want to place queen at ith row and jth column
    # we can only place queen in 2Dlist such that queen doesn't kill each other 
    # for that we will use validating function.
    
    if valid(arr,curr_pos,col):
      arr[curr_pos][col] = 1
      NQueens(arr,length,curr_pos+1)
      arr[curr_pos][col] = 0
  
  return
    
def main():

  size_of_matrix = 4
  
  if size_of_matrix == 1:
    print(["Q"])
    return
  array = []
  for i in range(size_of_matrix):
    sol = [0]*size_of_matrix
    array.append(sol)

  n = len(array)
  NQueens(array,n,0)
  print(ans)
  

if __name__ == "__main__":
  main()