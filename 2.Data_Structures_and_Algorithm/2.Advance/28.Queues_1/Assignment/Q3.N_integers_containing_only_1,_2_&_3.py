"""
Q3. N integers containing only 1, 2 & 3
Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.
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
 [1, 2, 3]
Output 2:
 [1, 2, 3, 11, 12, 13, 21]

Example Explanation
Explanation 1:
 Output denotes the first 3 integers that contains only digits 1, 2 and 3.
Explanation 2:
 Output denotes the first 3 integers that contains only digits 1, 2 and 3.
"""
from collections import deque

def find_Ath_NubmersInSeries(number):
    queue = deque()
    queue.append('1')
    queue.append('2')
    queue.append('3')
    list = ['1','2','3']
    count = 3
    for i in range(1,number):
        element = queue[0]
        queue.popleft()
        queue.append(element+'1')
        queue.append(element+'2')
        queue.append(element+'3')
        
        
        if number-count==1:
            list.append(element+'1')
            break
        elif number-count==2:
            list.append(element+'1')
            list.append(element+'2')
            break
        elif number-count==3:
            list.append(element+'1')
            list.append(element+'2')            
            list.append(element+'3')
            break
        else:
            list.append(element+'1')
            list.append(element+'2')            
            list.append(element+'3')
            
        count = count+ 3
        
    return list

number = 7
print(find_Ath_NubmersInSeries(number))