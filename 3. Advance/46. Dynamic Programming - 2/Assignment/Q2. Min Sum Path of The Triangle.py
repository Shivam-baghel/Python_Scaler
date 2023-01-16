""" 
Q2. Min Sum Path in Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
Adjacent numbers for jth number of row i is jth and (j+1)th numbers of row i+1 is

Problem Constraints
|A| <= 1000
A[i] <= 1000

Input Format
First and only argument is the vector of vector A defining the given triangle

Output Format
Return the minimum sum

Example Input
Input 1:
 
A = [ 
         [2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]
    ]
Input 2:
 A = [ [1] ]

Example Output
Output 1:
 11
Output 2:
 1

Example Explanation
Explanation 1:
 The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Explanation 2:
 Only 2 can be collected.
 
"""
import sys
sys.setrecursionlimit(10**5)
""" This my approach which is wrong find where it is going wrong"""
def main():
    A = [ 
            [2],
           [3, 4],
         [6, 5, 7],
        [4, 1, 8, 3]
        ]

    # length of the list of rows in each row
    length_row = len(A)

    # to store the max value of each column
    B = [0]*length_row
    # for loop to find the max value between columns of two rows.
    for row in range(length_row):
        B[row] = min(A[row])

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
def secMain():
    # a = [8, 9, 3, 8, 0, 2, 4, 8, 3, 9, 0, 5, 2, 2, 7, 3, 7, 9, 0, 2, 3, 9, 9, 7, 0, 3, 9, 8, 6, 5, 7, 6, 2, 7, 0, 3, 9]
    a = [ 
        [2],
        [3, 4],
        [6, 5, 7],
    [4, 1, 8, 3]
    ]
    def minimumTotal(A):
        dp = [0] * (len(A)+1)

        for row in A[::-1]:
            for i, v in enumerate(row):
                dp[i] = v + min(dp[i],dp[i+1])
        return dp[0]
    print(minimumTotal(a))
    return
if __name__ == "__main__":
    # main()
    secMain()
