"""
Q3. Count Increasing Triplets
Unsolved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints is now penalty free
Use Hint
Problem Description
You are given an array A of N elements. Find the number of triplets i,j and k such that i<j<k and A[i]<A[j]<A[k]


Problem Constraints
1 <= N <= 103
1 <= A[i] <= 109


Input Format
First argument A is an array of integers.


Output Format
Return an integer.


Example Input
Input 1:
A = [1, 2, 4, 3]
Input 2:
A = [2, 1, 2, 3]


Example Output
Output 1:
2
Output 2:
1


Example Explanation
For Input 1:
The triplets that satisfy the conditions are [1, 2, 3] and [1, 2, 4].
For Input 2:

The triplet that satisfy the conditions is [1, 2, 3].
"""


def triplets(A: list):
    arr = A
    n = len(A)
    result = 0
    for i in range(n):
        left = 0
        right = 0
        for j in range(i):
            if arr[j] < arr[i]:
                left += 1
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                right += 1
        result += (left * right)

    return result


if __name__ == '__main__':
    A = [1, 2, 4, 3]
    print(triplets(A))
