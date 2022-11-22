"""
279. Perfect Squares
Medium

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12

Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13

Output: 2
Explanation: 13 = 4 + 9.

Constraints:

1 <= n <= 104
"""
#Here DP and memorization concept is used.
import math

""" 
I still don't know how to do it. Providing a video link below for better understanding.

explained link: https://leetcode.com/problems/perfect-squares/discuss/2838408/PythonC%2B%2BJavaRust-faster-than-99-math-%2B-DP-%2B-BONUS-ONE-LINER-(explained)

Video Link: https://www.youtube.com/watch?v=ueN5KQMpVzQ

Code Link: https://ide.geeksforgeeks.org/399efe29-b898-4069-8c13-24508f1c9479
"""
def numSquares(n: int) -> int:
    
    if math.isqrt(n)**2 == n : return 1               # [1] already a square
    
    for i in range(1,math.isqrt(n)+1):                # [2] check pairs of squares
        if (j := n - i**2) == math.isqrt(j)**2:
            return 2
        
    while n % 4 == 0 : n /= 4                    # [3] well, it's maths, namely,
    if    n % 8 != 7 : return 3                  #     the Legendre's theorem
    
    return 4                                     # [4] the only remaining option

number = int(input())
print(numSquares(number))