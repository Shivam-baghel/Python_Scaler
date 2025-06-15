"""
Q1. Perfect Numbers
Given an integer A, you have to find the Ath Perfect Number.A Perfect Number has the following properties: It comprises only 1 and 2.
The number of digits in a Perfect number is even. It is a palindrome number.
For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.

Problem Constraints
1 <= A <= 100000

Input Format
The only argument given is an integer A.

Output Format
Return a string that denotes the Ath Perfect Number.

Example Input
Input 1:
 A = 2
Input 2:
 A = 3

Example Output
Output 1:
 22
Output 2:
 1111

Example Explanation
Explanation 1:
First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221

Explanation 2:
First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
"""
from collections import deque
import collections

def isPalindrome(string:str):
    """ This is a plaindrome function which checks if a given string is palindrome or not and returns True or False accordingly.

    Args:
        string (string): The function accepts arguments in string.

    Returns:
        Boolean: returns True or False.
    """
    if string == string[::-1]:
        return True
    return False

def find_Ath_PerfectNumber(number:int):
    """This is function to return Ath perfect Number. The persfect Number is explained in above question.

    Args:
        number (Integer): Accepts the number in Integer.

    Returns:
        String:  The string that denotes Ath perfect Number
    """    
    
    queue = deque()
    queue.append('1')
    queue.append('2')
    # n = 1<<number
    for i in range(number):
        element = queue[i]
        
        queue.append(element+'1')
        queue.append(element+'2')
        
    
    count = 0
    # for i in range(len(queue)):
    #     length = len(queue[i])
        
    # if length % 2 == 0 and isPalindrome(queue[i]):
    #         count +=1
            
    #         if count == number:
    #             return queue[i]
    
    """Explained in hint"""
    
    string = queue[number-1]
    rev = ''.join(reversed(string))
    
    return string+rev
    
    # for i in range(len(queue)):
        
        
            

n = 40
print(find_Ath_PerfectNumber(n))