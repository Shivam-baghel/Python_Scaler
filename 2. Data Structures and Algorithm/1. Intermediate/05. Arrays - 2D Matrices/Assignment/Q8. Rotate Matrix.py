""" 
Q8. Rotate Matrix

You are given a n x n 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.

Note: If you end up using an additional array, you will only receive partial score.

Problem Constraints
1 <= n <= 1000

Input Format
First argument is a 2D matrix A of integers

Output Format
Return the 2D rotated matrix.

Example Input
Input 1:

 [
    [1, 2],
    [3, 4]
 ]
Input 2:

 [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]


Example Output
Output 1:

 [
    [3, 1],
    [4, 2]
 ]
Output 2:

 [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
 ]


Example Explanation
Explanation 1:

 After rotating the matrix by 90 degree:
 1 goes to 2, 2 goes to 4
 4 goes to 3, 3 goes to 1
Explanation 2:

 After rotating the matrix by 90 degree:
 1 goes to 3, 3 goes to 9
 2 goes to 6, 6 goes to 8
 9 goes to 7, 7 goes to 1
 8 goes to 4, 4 goes to 2
"""


def rotate_matrix(arr):
   # for anti clockwise
   # idea here is first we have to transpose the matrix and then we have swap first row with last row.
   # then second row
   # with second last row and soo on.

   # # To Transpose matrix
   # n = len(A)
   # for i in range(n):
   #     for j in range(i):
   #         A[i][j],A[j][i] = A[j][i],A[i][j]

   # # To swap rows

   # for i in range(n//2):
   #     for j in range(n):
   #         A[i][j],A[n-1-i][j] = A[n-1-i][j],A[i][j]

   # return A

   n = len(arr)
   for i in range(1, n):
      for j in range(i):
         arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
   for i in arr:
      i.reverse()
   return arr


if __name__ == '__main__':
   A =  [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
         ]

   print(rotate_matrix(A))