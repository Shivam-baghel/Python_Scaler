""" 
Q2. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.

A gray code sequence must begin with 0.


Problem Constraints

1 <= A <= 16


Input Format

The first argument is an integer A.


Output Format

Return an array of integers representing the gray code sequence.


Example Input

Input 1:

A = 2
Input 1:

A = 1


Example Output

output 1:

[0, 1, 3, 2]
output 2:

[0, 1]


Example Explanation

Explanation 1:

for A = 2 the gray code sequence is:
    00 - 0
    01 - 1
    11 - 3
    10 - 2
So, return [0,1,3,2].
Explanation 1:

for A = 1 the gray code sequence is:
    00 - 0
    01 - 1
So, return [0, 1].

"""


def grayCode(A):
    if A == 1:
        base = []
        base.append(0)
        base.append(1)
        return base
    rres = grayCode(A - 1)
    mres = []
    for i in range(0, len(rres)):
        mres.append(rres[i])
    for i in range(len(rres) - 1, -1, -1):
        mres.append(2 ** (A - 1) + rres[i])
    return mres
