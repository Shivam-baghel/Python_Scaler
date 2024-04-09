""" 
Q1. Ath Magical Number

You are given three positive integers, A, B, and C.
Any positive integer is magical if divisible by either B or C.
Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.

Note: Ensure to prevent integer overflow while calculating.

Problem Constraints
1 <= A <= 109
2 <= B, C <= 40000

Input Format
The first argument given is an integer A.
The second argument given is an integer B.
The third argument given is an integer C.

Output Format
Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.

Example Input
Input 1:

 A = 1
 B = 2
 C = 3
Input 2:

 A = 4
 B = 2
 C = 3


Example Output
Output 1:

 2
Output 2:

 6


Example Explanation
Explanation 1:

 1st magical number is 2.
Explanation 2:

 First four magical numbers are 2, 3, 4, 6 so the 4th magical number is 6.
"""


def computeGCD(x, y):
    while y:
        x, y = y, x % y
    return x
    
mod = 1000000007


def Ath_magical_number( A, B, C):
    global mod
    low = 2
    high = A * min(B, C)
    ans = 0
    # lcm of B and C
    lc = (B * C) // computeGCD(B, C)
    while low <= high:
        mid = low + (high - low) // 2
        # f(x) = x / B + x / C - x / lcm(B, C)
        ct = mid // B + mid // C - mid // lc
        if ct >= A:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    ans %= mod
    return ans