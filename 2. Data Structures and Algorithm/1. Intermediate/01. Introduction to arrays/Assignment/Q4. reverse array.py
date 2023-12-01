"""
Q4. Reverse the Array

You are given a constant array A.
You are required to return another array which is the reversed form of the input array.


Problem Constraints
1 <= A.size() <= 10000
1 <= A[i] <= 10000

Input Format
First argument is a constant array A.

Output Format
Return an integer array.

Example Input
Input 1:

A = [1,2,3,2,1]
Input 2:

A = [1,1,10]


Example Output
Output 1:

 [1,2,3,2,1]
Output 2:

 [10,1,1]


Example Explanation
Explanation 1:

Reversed form of input array is same as original array
Explanation 2:

Clearly, Reverse of [1,1,10] is [10,1,1]
"""


def reverse(A):
    A = list(A)
    lastIndex = len(A) - 1

    for i in range(len(A) // 2):
        A[i], A[lastIndex] = A[lastIndex], A[i]
        lastIndex -= 1

    return A


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    print(reverse(a))
