""" 
Q3. Max Sum Without Adjacent Elements
Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.
Note: You can choose more than 2 numbers.

Problem Constraints
1 <= N <= 20000
1 <= A[i] <= 2000

Input Format
The first and the only argument of input contains a 2d matrix, A.

Output Format
Return an integer, representing the maximum possible sum.

Example Input

Input 1:

 A = [   
        [1]
        [2]    
     ]
Input 2:

 A = [   
        [1, 2, 3, 4]
        [2, 3, 4, 5]    
     ]

Example Output
Output 1:
 2
Output 2:
 8

Example Explanation
Explanation 1:
 We will choose 2.
Explanation 2:
 We will choose 3 and 5.

"""

"""
The Idea Behind My approach. 
we are given an 2*n matrix. and we can't go for adjacent horiontal,vertical or diagonal values in 2*n matrix. we have to choose max value between the two rows to find the max sum.
so why not convert 2*n matrix to a 1D matrix just simply choose max between the columns of the 2 rows and store the max value in columns of the 1D list.
after that use max subsequence program to find the ans.

"""
import sys
sys.setrecursionlimit(10**5)

def maxSumWithOutAdjElements():
   A = [   
      [1, 2, 3, 4],
      [2, 3, 4, 5]    
   ]
   
   # length of the list of columns in each row
   length_col = len(A[0])
   
   # to store the max value of each column
   B = [0]*length_col
   # for loop to find the max value between columns of two rows.
   for col in range(length_col):
      B[col] = max(A[0][col],A[1][col])
   
   # print(B)
   # length of the updated array.
   num = len(B)
   # dp list to store the ans values.
   dp = [-1]*(num)
   
   # function to find solution using dynamic programming.
   def MaxSub(arr,i):
      # if ith position is 0 return 0
      if i < 0:
            return 0
      
      # if dp value is checked for the first time on the ith position.
      if dp[i] == -1:
            # find and store the max value which could be the ans 
            dp[i] = max(MaxSub(arr,i-1) , MaxSub(arr,i-2)+arr[i])
      
      return dp[i]


   print(MaxSub(B,num-1))
   
   return #MaxSub(B,num-1)

if __name__ == "__main__":
   maxSumWithOutAdjElements()
   
