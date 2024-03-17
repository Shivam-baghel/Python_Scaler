""" 
Q1. Matrix Search
Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A.
This matrix A has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

NOTE: Rows are numbered from top to bottom, and columns are from left to right.

Problem Constraints
1 <= N, M <= 1000
1 <= A[i][j], B <= 106

Input Format
The first argument given is the integer matrix A.
The second argument given is the integer B.

Output Format
Return 1 if B is present in A else, return 0.

Example Input
Input 1:
A = [ 
      [1,   3,  5,  7]
      [10, 11, 16, 20]
      [23, 30, 34, 50]  
    ]
B = 3
Input 2:
A = [   
      [5, 17, 100, 111]
      [119, 120, 127, 131]    
    ]
B = 3

Example Output
Output 1:
1
Output 2:
0

Example Explanation
Explanation 1:
 3 is present in the matrix at A[0][1] position so return 1.
Explanation 2:
 3 is not present in the matrix so return 0.
"""

"""
Hint : 
Assume the matrix as a Flattened sorted array.
This array will have m*n elements, where m is the number of rows and n is the number of columns.
Since the matrix is sorted, we can apply a binary search algorithm on this flattened array to efficiently search for the target number.
Initialize the search space by setting the low index as 0 and the high index as m*n - 1.
Apply Binary search on the flattened array.
Translate the middle index to the corresponding matrix row and column.
Use the formulas: row = int(mid / n) and col = int(mid % n).
Compare the middle element with the target number.
Update the search space based on the comparison.
Repeat until the target is found or search space is exhausted.
Return 1 if the target is found, otherwise return 0.
"""


def matrix_search(mat: list, k: int):
    row = len(mat)
    col = len(mat[0])

    low = 0
    high = (row * col) - 1

    while low <= high:
        mid = (high + low) // 2
        i = mid // col
        j = mid % col

        if mat[i][j] == k:
            return 1
        elif mat[i][j] <= k:
            low = mid + 1
        else:
            high = mid - 1

    return 0


if __name__ == '__main__':
    A = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    B = 3
    print(matrix_search(A, B))
