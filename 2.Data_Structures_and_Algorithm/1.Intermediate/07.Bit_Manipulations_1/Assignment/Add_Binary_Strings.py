""" 
Q2. Add Binary Strings

Given two binary strings A and B. Return their sum (also a binary string).

Problem Constraints
1 <= length of A <= 105
1 <= length of B <= 105
A and B are binary strings

Input Format
The two argument A and B are binary strings.

Output Format
Return a binary string denoting the sum of A and B

Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"


Example Output

Output 1:
"111"
Output 2:
"1000"


Example Explanation

For Input 1:
The sum of 100 and 11 is 111.
For Input 2:

The sum of 110 and 10 is 1000.
"""


def addBinary( A, B):
    N = max(len(A), len(B))
    # Filling 0 infront of strings to get same length string
    A = A.zfill(N)
    B = B.zfill(N)
    # Performming addition
    carry = 0
    res = ""
    for i in range(N - 1, -1, -1):
        _sum = carry
        _sum += 1 if A[i] == "1" else 0
        _sum += 1 if B[i] == "1" else 0
        res = ("0" if _sum % 2 == 0 else "1") + res
        carry = 0 if _sum < 2 else 1
    if carry != 0:
        res = "1" + res
    return res
