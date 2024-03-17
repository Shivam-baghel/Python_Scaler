"""
Q2. Check Palindrome - II
Given a string A consisting of lowercase characters.
Check if characters of the given string can be rearranged to form a palindrome.
Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

Problem Constraints
1 <= |A| <= 105

A consists only of lower-case characters.

Input Format
First argument is an string A.

Output Format
Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

Example Input
Input 1:
 A = "abcde"
Input 2:
 A = "abbaee"

Example Output
Output 1:
 0
Output 2:
 1

Example Explanation
Explanation 1:
 No possible rearrangement to make the string palindrome.
Explanation 2:
 Given string "abbaee" can be rearranged to "aebbea" to form a palindrome.
"""


# @param A : string
# @return an integer
def checkPalindrome(A):
    # Create a freq map of lowercase characters
    freq = {}
    for i in A:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    countOfodd = 0
    for j in range(len(A)):
        if freq[A[j]] % 2 == 0:
            continue
        else:
            countOfodd += 1
            freq[A[j]] -= 1

    if countOfodd > 1:
        return 0
    else:
        return 1


A = "yzfbzbyyrurquqf"
print(checkPalindrome(A))
