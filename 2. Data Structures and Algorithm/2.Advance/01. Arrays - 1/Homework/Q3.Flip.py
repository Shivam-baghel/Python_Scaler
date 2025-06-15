""" 
Q3. Flip

You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.

Problem Constraints
1 <= size of string <= 100000

Input Format
First and only argument is a string A.

Output Format
Return an array of integers denoting the answer.

Example Input

Input 1:
A = "010"

Input 2:
A = "111"

Example Output

Output 1:
[1, 1]

Output 2:
[]


Example Explanation
Explanation 1:

A = "010"

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | "110"
[1 2]          | "100"
[1 3]          | "101"
[2 2]          | "000"
[2 3]          | "001"

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Explanation 2:

No operation can give us more than three 1s in final string. So, we return empty array [].
"""

def flip(array):
    n = len(array)
    nums = [0]*n
    for i in range(n):
        if array[i] == '1':
            nums[i]= -1
        else:
            nums[i] = 1
    
    currSum , bestSum = 0,0
    left , right , index = 0,-1,0
    
    for j in range(n):
        currSum += nums[j]
        if currSum < 0:
            currSum = 0
            index = j+1
        elif currSum  > bestSum:
            left = index
            right = j
            bestSum = currSum
    
    if right != -1:
        return [left+1,right+1]
    else:
        return []
    
A = "010"   
print(flip(A))