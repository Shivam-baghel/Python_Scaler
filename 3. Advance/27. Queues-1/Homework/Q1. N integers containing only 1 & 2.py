"""
Q3. N integers containing only 1 & 2.
Given an integer, A. Find and Return first positive Ath integer containing only digits 1 and 2.
NOTE: All the A integers will fit in 32-bit integers.

Problem Constraints
1 <= A <= 29500

Input Format
The only argument given is integer A.

Output Format
Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.

Example Input
Input 1:
 A = 3
Input 2:
 A = 7

Example Output
Output 1:
 11
Output 2:
 112

Example Explanation
Explanation 1:
 Output denotes the first 3 integers that contains only digits 1 and 2. are [1, 2, 11], A = 3 output is 11.
Explanation 2:
 Output denotes the first 3 integers that contains only digits 1 and 2. are [1, 2, 11, 12, 21, 111, 112], A = 7 output is 112
"""

from collections import deque

def findAthNumberInSeries(number:int):
    queue = deque()
    queue.append('1')
    queue.append('2')
    
    for i in range(1,number):
        element = queue[0]
        queue.popleft()
        queue.append(element+"1")
        queue.append(element+"2")

    return queue[0]

number = 3
print(findAthNumberInSeries(number))
        