""" 
Q3. Max Continuous Series of 1s

Given a binary array A, find the maximum sequence of continuous 1's that can be formed by replacing at-most B zeroes.
For this problem, return the indices of maximum continuous series of 1s in order.
If there are multiple possible solutions, return the sequence which has the minimum start index.

Problem Constraints
0 <= B <= 105
1 <= size(A) <= 105
0 <= A[i] <= 1

Input Format
First argument is an binary array A.
Second argument is an integer B.

Output Format
Return an array of integers denoting the indices(0-based) of 1's in the maximum continuous series.

Example Input
Input 1:

 A = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
 B = 1
Input 2:

 A = [1, 0, 0, 0, 1, 0, 1]
 B = 2


Example Output
Output 1:

 [0, 1, 2, 3, 4]
Output 2:

 [3, 4, 5, 6]


Example Explanation
Explanation 1:

 Flipping 0 present at index 2 gives us the longest continous series of 1's i.e subarray [0:4].
Explanation 2:

 Flipping 0 present at index 3 and index 5 gives us the longest continous series of 1's i.e subarray [3:6].
"""


def maxone(self, A, B):
    n = len(A)
    left = 0
    right = 0
    noZerosInWindow = 0
    if A[right] == 0:
        noZerosInWindow += 1
    bestLeft = 0
    bestRight = 0

    while right < n:
        # add an element if the number of 0's <= B
        if noZerosInWindow <= B:
            right += 1
            if right < n and A[right] == 0:
                noZerosInWindow += 1
        # remove an element if the number of 0's > B
        if noZerosInWindow > B:
            if A[left] == 0:
                noZerosInWindow -= 1
            left += 1

        if right >= n:
            if n - 1 - left > bestRight - bestLeft:
                bestLeft = left
                bestRight = n - 1
        elif right - left > bestRight - bestLeft:
            bestLeft = left
            bestRight = right

    if bestRight > n - 1:
        bestRight = n - 1
    ans = [i for i in range(bestLeft, bestRight + 1)]
    return ans
