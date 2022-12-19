"""
Problem Description
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.
NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Problem Constraints
2 <= |A| <= 2000000
0 <= A[i] <= INTMAX

Input Format
The first and only argument of input contains an integer array A.
Output Format
Return a single integer denoting the single element.

Example Input
Input 1:
 A = [1, 2, 2, 3, 1]
Input 2:
 A = [1, 2, 2]

Example Output
Output 1:
 3
Output 2:
 1
Example Explanation
Explanation 1:
 3 occurs once.
Explanation 2:
 1 occurs once.

"""
def singleNumber(arr:tuple):
    lengthOftuple = len(arr)
    ans = 0
    for i in range(lengthOftuple):
        ans = ans^arr[i]        # we have used the property of xor.if we have xor of two same no. it will give 0 and if there is only 1 different no. that no xor 0 will always give that no.
    return ans

A_tuple = tuple(map(int,input().split()))
print(singleNumber(A_tuple))