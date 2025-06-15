"""
Q1. Common Elements
Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.
NOTE:
Each element in the result should appear as many times as it appears in both arrays.
The result can be in any order.

Problem Constraints
1 <= N, M <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A of size N.
Second argument is an integer array B of size M.

Output Format
Return an integer array denoting the common elements.

Example Input
Input 1:
 A = [1, 2, 2, 1]
 B = [2, 3, 1, 2]
Input 2:
 A = [2, 1, 4, 10]
 B = [3, 6, 2, 10, 10]

Example Output
Output 1:
 [1, 2, 2]
Output 2:
 [2, 10]

Example Explanation
Explanation 1:
 Elements (1, 2, 2) appears in both the array. Note 2 appears twice in both the array.
Explantion 2:
 Elements (2, 10) appears in both the array.
"""


def commonElements(A, B):
    """this function returns the common elements between two integer arrays.

    Args:
        A (List): Integer array of size N.
        B (List): Integer array of size M.

    Returns:
        _type_: Integer array denoting the common elements.
    """
    # if len(A) <= len(B):
    #     n = len(A)
    # else:
    #     n = len(B)

    # res = []
    # for i in range(n):
    #     if A[i] in B:
    #         B.remove(A[i])
    #         res.append(A[i])

    # 2nd idea
    dictionary = {}
    res = []
    n1 = len(A)
    n2 = len(B)

    for i in range(n2):
        if B[i] in dictionary:
            dictionary[B[i]] += 1
        else:
            dictionary[B[i]] = 1

    for i in range(n1):
        if A[i] in dictionary and dictionary[A[i]] > 0:
            res.append(A[i])
            dictionary[A[i]] -= 1
    return res


A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
print(commonElements(A, B))
