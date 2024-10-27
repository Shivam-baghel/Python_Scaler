""" 
Q3. Reverse Bits
Reverse the bits of an 32 bit unsigned integer A.

Problem Constraints
0 <= A <= 232

Input Format
First and only argument of input contains an integer A.

Output Format
Return a single unsigned integer denoting the decimal value of reversed bits.

Example Input
Input 1:

 0
Input 2:

 3


Example Output

Output 1:

 0
Output 2:

 3221225472


Example Explanation

Explanation 1:

        00000000000000000000000000000000    
=>      00000000000000000000000000000000
Explanation 2:

        00000000000000000000000000000011    
=>      11000000000000000000000000000000
"""


def reverse( A):
    num = len(str(bin(A))) 
    b = 0
    i=1
    while (A>0):
        y = A&1
        mul = 1<<(32-i)
        b += (y*mul)
        A = A>>1
        i+=1

    return b