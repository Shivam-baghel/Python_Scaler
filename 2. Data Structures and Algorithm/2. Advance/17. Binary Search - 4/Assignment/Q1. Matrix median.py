""" 
Q1. Matrix Median

Given a matrix of integers A of size N x M in which each row is sorted.

Find and return the overall median of matrix A.

NOTE: No extra memory is allowed.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints

1 <= N, M <= 10^5
1 <= N*M <= 10^6
1 <= A[i] <= 10^9

N*M is odd


Input Format

The first and only argument given is the integer matrix A.


Output Format

Return the overall median of matrix A.


Example Input

Input 1:

A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ] 
Input 2:

A = [   [5, 17, 100]    ]


Example Output

Output 1:

 5 
Output 2:

 17


Example Explanation

Explanation 1:

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5. 
Explanation 2:

Median is 17.
"""


# search range is smallest value to larger value in matrix, since the matrix is sorted it would be easy to find.
def getSearchSpace(matrix):
    minVal = float("inf")
    maxVal = float("-inf")
    for row in matrix:
        if minVal > row[0]:
            minVal = row[0]
        if maxVal < row[-1]:
            maxVal = row[-1]
    return minVal, maxVal


# In each row we need to find number count which is lesser than the mid value
def countSmallerThanEqualToMid(row, mid):
    l, r = 0, len(row) - 1

    while l <= r:
        m = (l + r) >> 1
        if row[m] <= mid:
            l = m + 1
        else:
            r = m - 1
    return l


def findMedian(A):
    row, col = len(A), len(A[0])
    left, right = getSearchSpace(A)

    while left <= right:
        count = 0
        mid = (left + right) >> 1 # type: ignore
        for i in range(row):
            count += countSmallerThanEqualToMid(A[i], mid)
        # since we know the median will be present at center, hence half the size of matrix will be the position.
        if count <= (row * col) // 2:
            left = mid + 1
        else:
            right = mid - 1

    return left
