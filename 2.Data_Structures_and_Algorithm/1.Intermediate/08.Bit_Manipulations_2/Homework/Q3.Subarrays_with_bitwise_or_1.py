""" 
Q3. Subarrays with Bitwise OR 1

Given an array B of length A with elements 1 or 0. Find the number of subarrays such that the bitwise OR of all the elements present in the subarray is 1.
Note : The answer can be large. So, return type must be long.

Problem Constraints
1 <= A <= 105

Input Format
The first argument is a single integer A.
The second argument is an integer array B.

Output Format
Return the number of subarrays with bitwise array 1.

Example Input

Input 1:
 A = 3
B = [1, 0, 1]
Input 2:
 A = 2
B = [1, 0]


Example Output

Output 1:
5
Output2:
2


Example Explanation

Explanation 1:
The subarrays are :- [1], [0], [1], [1, 0], [0, 1], [1, 0, 1]
Except the subarray [0] all the other subarrays has a Bitwise OR = 1
Explanation 2:
The subarrays are :- [1], [0], [1, 0]
Except the subarray [0] all the other subarrays has a Bitwise OR = 1
"""


def solve(A, B):
    n = len(B)
    t = A * (A + 1) // 2  # counting total subarray
    cnt = 0
    sum = 0
    for i in range(n):
        if (
            B[i] == 0
        ):  # by counting zeroes we can subtract the total subarray with the subarray with only Zero
            cnt += 1
        else:
            sum += cnt * (cnt + 1) // 2
            cnt = 0
    if cnt >= 1:
        sum += cnt * (cnt + 1) // 2
    return t - sum
