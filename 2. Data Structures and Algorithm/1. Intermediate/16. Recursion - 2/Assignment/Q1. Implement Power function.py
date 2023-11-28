""" 
Q1. Implement Power Function

Implement pow(A, B) % C.
In other words, given A, B and C, Find (AB % C).
Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.


Problem Constraints
-109 <= A <= 109
0 <= B <= 109
1 <= C <= 109


Input Format
Given three integers A, B, C.


Output Format
Return an integer.


Example Input
Input 1:
A = 2
B = 3
C = 3
Input 2:
A = 3
B = 3
C = 1


Example Output
Output 1:
2
Output 2:
0


Example Explanation
Explanation 1:
23 % 3 = 8 % 3 = 2
Explanation 2:
33 % 1 = 27 % 1 = 0
"""

'''
the question is divided in two parts:
first we have to find out a to the power b:
ex a = 2, b = 3 then a^b = 2^3 = 8

second , we have to do the modulus of the result given by pow function with c.
ex c = 3, 8%3= 2
 ans would be 2.
'''


def pow(a, b):
    if b == 0:
        return 1

    return pow(a, b - 1) * a


def implementPow(a, b, c):
    powResult = pow(a, b)
    return powResult % 3


''' More efficient way is below '''


def power(x, y, mod):
    if y == 0:
        return 1 % mod
    if y == 1:
        return x % mod

    val = power(x, y // 2, mod)

    if y & 1:
        return (val % mod * val % mod * x % mod) % mod
    else:
        return (val % mod * val % mod) % mod


if __name__ == "__main__":
    a = 2
    b = 3
    c = 3
    print(implementPow(a, b, c))
    print(power(a, b, c))
