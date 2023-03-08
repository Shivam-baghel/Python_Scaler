"""
Q1. Make String Palindrome
Given a string A of size N consisting only of lowercase alphabets. The only operation allowed is to insert characters in the beginning of the string.
Find and return how many minimum characters are needed to be inserted to make the string a palindrome string.

Problem Constraints
1 <= N <= 106

Input Format
The only argument given is a string A.

Output Format
Return an integer denoting the minimum characters needed to be inserted in the beginning to make the string a palindrome string.

Example Input
Input 1:
 A = "abc"
Input 2:
 A = "bb"

Example Output
Output 1:
 2
Output 2:
 0

Example Explanation
Explanation 1:
 Insert 'b' at beginning, string becomes: "babc".
 Insert 'c' at beginning, string becomes: "cbabc".
Explanation 2:
 There is no need to insert any character at the beginning as the string is already a palindrome.
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

def makePalindrome(A):

    newString = A+'@'+A[::-1]
    length = len(newString)
    lps = lpsfun(newString,length)

    ans = len(A)-lps[2*len(A)]
    
    return ans

A="abc"
print(makePalindrome(A))