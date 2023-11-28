""" 
Q3. Column Sum

You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.

Problem Constraints
1 <= A.size() <= 103
1 <= A[i].size() <= 103
1 <= A[i][j] <= 103

Input Format
First argument is a 2D array of integers.(2D matrix).

Output Format
Return an array containing column-wise sums of original matrix.

Example Input
Input 1:

[1,2,3,4]
[5,6,7,8]
[9,2,3,4]


Example Output
Output 1:

{15,10,13,16}


Example Explanation
Explanation 1

Column 1 = 1+5+9 = 15
Column 2 = 2+6+2 = 10
Column 3 = 3+7+3 = 13
Column 4 = 4+8+4 = 16
"""


def column_sum(A):
    lengthOfColumn = len(A[0])
    lengthOfRow = len(A)
    res = []
    for j in range(lengthOfColumn):
        inner_sum = 0
        for i in range(lengthOfRow):
            inner_sum = inner_sum + A[i][j]

        res.append(inner_sum)

    return res



if __name__ == '__main__':
    a = [
        [1,2,3,4],
        [5,6,7,8],
        [9,2,3,4]
        ]
    print(column_sum(a))
