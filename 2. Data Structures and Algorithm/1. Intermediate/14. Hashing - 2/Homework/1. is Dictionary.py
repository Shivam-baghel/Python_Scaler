"""
Q 1
Q1. Is Dictionary?
Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.

Problem Constraints
1 <= N, length of each word <= 105

Sum of the length of all words <= 2 * 106

Input Format
The first argument is a string array A of size N.

The second argument is a string B of size 26, denoting the order.

Output Format
Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.

Example Input
Input 1:
 A = ["hello", "scaler", "interviewbit"]
 B = "adhbcfegskjlponmirqtxwuvzy"
Input 2:
 A = ["fine", "none", "no"]
 B = "qwertyuiopasdfghjklzxcvbnm"


Example Output
Output 1:
 1
Output 2:
 0


Example Explanation
Explanation 1:

 The order shown in string B is: h < s < i for the given words. So return 1.
Explanation 2:

 "none" should be present after "no". Return 0.

"""


def isItDictionary(A, B):
    """This function is used to check for lexigraphic words.

    Args:
        A (_type_): _description_
        B (_type_): _description_

    Returns:
        _type_: _description_
    """

    dictV = {}
    for i, n in enumerate(B):
        dictV[B[i]] = i
    for i in range(1, len(A)):
        word1 = A[i - 1]
        word2 = A[i]
        i = 0
        greater = False
        while (i < len(word1)) and (i < len(word2)):
            if dictV[word1[i]] > dictV[word2[i]]:
                return 0
            elif dictV[word1[i]] == dictV[word2[i]]:
                i += 1
            else:
                greater = True
                break
        if not greater and len(word1) > len(word2):
            return 0
    return 1
