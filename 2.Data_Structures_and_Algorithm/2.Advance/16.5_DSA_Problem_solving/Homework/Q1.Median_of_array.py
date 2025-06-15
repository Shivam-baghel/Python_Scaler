""" 
Q1. Median of Array

There are two sorted arrays A and B of sizes N and M respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

NOTE:

The overall run time complexity should be O(log(m+n)).
IF the number of elements in the merged array is even, then the median is the average of (n/2)th and (n/2+1)th element. For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5.


Problem Constraints

1 <= N + M <= 2*106



Input Format

The first argument is an integer array A of size N.
The second argument is an integer array B of size M.



Output Format

Return a decimal value denoting the median of two sorted arrays.



Example Input

Input 1:

 A = [1, 4, 5]
 B = [2, 3]
Input 2:

 A = [1, 2, 3]
 B = [4]


Example Output

Output 1:

 3.0
Output 2:

 2.5


Example Explanation

Explanation 1:

 The median of both the sorted arrays will be 3.0.
Explanation 2:

 The median of both the sorted arrays will be (2+3)/2 = 2.5.

"""


def findMedianSortedArrays(A, B):
    if len(A) < len(B):
        A, B = B, A
    a = len(A)
    b = len(B)
    l = 0
    r = b - 1
    total = a + b
    half = (a + b) // 2

    while True:
        midB = (l + r) // 2
        midA = half - midB - 2
        Aleft = A[midA] if midA >= 0 else float("-infinity")
        Aright = A[midA + 1] if midA < a - 1 else float("infinity")
        Bleft = B[midB] if midB >= 0 else float("-infinity")
        Bright = B[midB + 1] if midB < b - 1 else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2 == 0:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            else:
                return min(Aright, Bright)
        elif Bleft > Aright:
            r = midB - 1
        else:
            l = midB + 1
