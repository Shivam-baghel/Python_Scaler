""" 
Q2. Hidden Pattern
Given two strings - a text A and a pattern B, having lower-case alphabetic characters. You have to determine the number of occurrences of pattern B in text A as its substring. i.e. the number of times B occurs as a substring in A.

Problem Constraints
1 <= |B| <= |A| <= 105

Input Format
First argument is a string A
Second argument is a string B

Output Format
Return the number of occurrences.

Example Input
Input 1:
 A = "abababa"
 B = "aba" 
Input 2:
 A = "mississipi"
 B = "ss" 
Input 3:
 A = "hello" 
 B = "hi" 

Example Output
Output 1:
 3 
Output 2:
 2 
Output 3:
 0 

Example Explanation
Explanation 1:
 A has 3 substrings equal to B - A[1, 3], A[3, 5] and A[5, 7] 
Explanation 2:
 B occurs two times in A - A[3, 4], A[6, 7]. 
Explanation 3:
 B does not occur in A as a substring.
"""

def lpsfun(string,length):
    lpsList =[0]*length
    
    for i in range(1,length):
        x = lpsList[i-1]
        while string[i] != string[x] :
            if x == 0:
                x =-1
                break
            
            x = lpsList[x-1]
        lpsList[i] = x+1
    
    return lpsList

def hiddenPattern(A, B):
    pattern = B 
    text = A

    lengthOfPattern = len(pattern)
    combinationOfAB = pattern+'@'+text
    lengthOfcombination = len(combinationOfAB)

    lps = lpsfun(combinationOfAB,lengthOfcombination)

    count = 0
    for i in range(len(lps)):
        if lps[i]==lengthOfPattern:
            count +=1
    
    return count

A = "abababa"
B = "aba" 
print(hiddenPattern(A,B))