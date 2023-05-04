""" 
Q1. Add One To Number
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :

Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
A: For the purpose of this question, YES
Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

Problem Constraints
1 <= size of the array <= 1000000

Input Format
First argument is an array of digits.

Output Format
Return the array of digits after adding one.

Example Input
Input 1:
[1, 2, 3]

Example Output
Output 1:
[1, 2, 4]

Example Explanation

Explanation 1:
Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
"""

def plusOne(self, A):

    def ReverseList(arrayOfInteger:list):
        i = 0
        j = len(arrayOfInteger)-1
        while i<j:
            arrayOfInteger[i],arrayOfInteger[j] = arrayOfInteger[j],arrayOfInteger[i]
            i += 1
            j -= 1
        
        return arrayOfInteger

    def RemoveTrailingZero(array:list):
        i = 0
        j = len(array)
        n = len(array)
        for l in range(n-1,-1,-1):
            if array[l] != 0:
                break
            j = l
        
        return array[i:j]


# idea behind the solution is:
    # change the number to one based indexing for easier execution
    # reverse the digits using reverse list function by creating it
    # keep addone and carry equal to 1,0. take each digit on reverse list add "addone and carry" the find the carry if there is. keep doing it untill carry and addone becomes zero.
    # remove the trailling zeros and return the reversed list again.
    lengthOfA = len(A)
    B = [0]*(lengthOfA+1)
    B[0]=0
    for i in range(1,len(B)):
        B[i]= A[i-1]
        
    carry = 0
    addOne = 1
    B = ReverseList(B)
    
    for i in range(len(B)):
        result = B[i] + addOne + carry
        B[i] = result % 10
        carry = result // 10
        if addOne > 0:
            addOne -= 1
    
    B = ReverseList(RemoveTrailingZero(B))
    return B 
