""" 
Q1. Check Palindrome

Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.

Note: A palindrome is a string that's the same when read forward and backward.

Problem Constraints
1 <= |A| <= 50000

String A consists only of lowercase letters.

Input Format
The first and only argument is a string A.

Output Format
Return 1 if the string A is a palindrome, else return 0.

Example Input
Input 1:

 A = "naman"
Input 2:

 A = "strings"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 "naman" is a palindomic string, so return 1.
Explanation 2:

 "strings" is not a palindrome, so return 0.
"""


def chkPalindrome(string: str, sIndex: int, eIndex: int):
    if sIndex >= eIndex:
        return 1

    if string[sIndex] == string[eIndex]:
        return chkPalindrome(string, sIndex + 1, eIndex - 1)

    return 0


def palindrome(string: str):
    end = len(string) - 1
    start = 0

    return chkPalindrome(string, start, end)


if __name__ == '__main__':
    a = 'naman'
    print(palindrome(a))
