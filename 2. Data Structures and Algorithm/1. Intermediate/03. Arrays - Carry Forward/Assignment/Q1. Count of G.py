""" 
Q1. Special Subsequences "AG"

You have given a string A having Uppercase English letters.
You have to find how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.

Problem Constraints
1 <= length(A) <= 105

Input Format
First and only argument is a string A.

Output Format
Return an integer denoting the answer.

Example Input
Input 1:
 A = "ABCGAG"
Input 2:
 A = "GAB"

Example Output
Output 1:
 3
Output 2:
 0

Example Explanation
Explanation 1:

 Subsequence "AG" is 3 times in given string 
Explanation 2:

 There is no subsequence "AG" in the given string.
"""

import math


def countOfAGPair(arr:list):
    modulo = int(math.pow(10,9)) + 7
    countOfg = 0
    ans = 0
    
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == 'G':
            countOfg += 1
        elif arr[i] == 'A':
            ans += countOfg
    
    
    return ans%modulo


a = "ABCGAG"
print(countOfAGPair(a))