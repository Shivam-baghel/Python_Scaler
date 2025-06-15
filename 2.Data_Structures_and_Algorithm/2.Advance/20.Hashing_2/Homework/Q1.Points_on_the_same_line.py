""" 
Q1. Points on same line

Given two arrays of integers A and B describing a pair of (A[i], B[i]) coordinates in a 2D plane. A[i] describe x coordinates of the ith point in the 2D plane, whereas B[i] describes the y-coordinate of the ith point in the 2D plane.

Find and return the maximum number of points that lie on the same line.

Problem Constraints
1 <= (length of the array A = length of array B) <= 1000
-105 <= A[i], B[i] <= 105

Input Format
The first argument is an integer array A.
The second argument is an integer array B.

Output Format
Return the maximum number of points which lie on the same line.

Example Input
Input 1:

 A = [-1, 0, 1, 2, 3, 3]
 B = [1, 0, 1, 2, 3, 4]
Input 2:

 A = [3, 1, 4, 5, 7, -9, -8, 6]
 B = [4, -8, -3, -2, -1, 5, 7, -4]


Example Output
Output 1:

 4
Output 2:

 2


Example Explanation
Explanation 1:

 The maximum number of point which lie on same line are 4, those points are {0, 0}, {1, 1}, {2, 2}, {3, 3}.
Explanation 2:

 Any 2 points lie on a same line.
"""


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def maxpointsonsameline(x, y):
    n = len(x)
    if n < 3:
        return n
    ans = 0
    curmax = 0
    overlap = 0
    vertical = 0
    for i in range(n):
        mp = {}
        curmax = 0
        overlap = 0
        vertical = 0
        for j in range(i + 1, n):
            if x[i] == x[j] and y[i] == y[j]:
                overlap += 1
            elif x[i] == x[j]:
                vertical += 1
            else:
                xdiff = x[j] - x[i]
                ydiff = y[j] - y[i]
                z = gcd(xdiff, ydiff)
                xdiff /= z
                ydiff /= z
                # mp stores the slope of the line between i-th and j-th point
                if mp.get((xdiff, ydiff)) == None:
                    mp[(xdiff, ydiff)] = 1
                else:
                    mp[(xdiff, ydiff)] += 1
                curmax = max(curmax, mp[(xdiff, ydiff)])
            curmax = max(curmax, vertical)
        ans = max(ans, curmax + overlap + 1)
    return ans


if __name__ == "__main__":

    A = [-1, 0, 1, 2, 3, 3]
    B = [1, 0, 1, 2, 3, 4]
    maxpointsonsameline(A, B)
