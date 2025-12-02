""" 
Q3. Regular Expression Match

Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

' ? ' : Matches any single character.
' * ' : Matches any sequence of characters (including the empty sequence).



The matching should cover the entire input string (not partial).




Problem Constraints

1 <= length(A), length(B) <= 104



Input Format

The first argument of input contains a string A.
The second argument of input contains a string B.



Output Format

Return 1 if the patterns match else return 0.



Example Input

Input 1:

 A = "aaa"
 B = "a*"
Input 2:

 A = "acz"
 B = "a?a"


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 Since '*' matches any sequence of characters. Last two 'a' in string A will be match by '*'.
 So, the pattern matches we return 1.
Explanation 2:

 '?' matches any single character. First two character in string A will be match. 
 But the last character i.e 'z' != 'a'. Return 0.
 
"""


def isMatch(A, B):
    string_T = A
    # change the pattern
    b = list(B)
    count = 0
    n = len(b)
    m = 0
    while m <= n - 1:
        if b[m] == "*":
            count += 1

            if count > 1:
                b.pop(m)
                count -= 1
                n = len(b)
                m -= 1
        if b[m] != "*":
            count = 0
        m += 1

    string_P = "".join(b)
    length_of_str1 = len(string_T)
    length_of_str2 = len(string_P)
    dp = []
    for i in range(length_of_str1):
        col = []
        for j in range(length_of_str2):
            col.append(-1)
        dp.append(col)

    def Regex(Text, Pattern, i, j):
        if i < 0 and j < 0:
            # text and pattern both are empty strings.
            return 1
        elif i < 0:
            for k in range(j + 1):
                if Pattern[k] != "*":
                    return 0
            return 1
        elif j < 0:
            return 0

        if dp[i][j] == -1:
            if Text[i] == Pattern[j] or Pattern[j] == "?":
                dp[i][j] = Regex(Text, Pattern, i - 1, j - 1)
            elif Pattern[j] == "*":
                dp[i][j] = Regex(Text, Pattern, i, j - 1) | Regex(
                    Text, Pattern, i - 1, j
                )
            else:
                dp[i][j] = 0

        return dp[i][j]

    return Regex(string_T, string_P, length_of_str1 - 1, length_of_str2 - 1)
    # s = A
    # p = B
    # if len(p) - p.count("*") > len(s):
    #     return 0
    # DP = [True] + [False] * len(s)
    # for c in p:
    #     if c == "*":
    #         for n in range(1, len(s) + 1):
    #             DP[n] = DP[n - 1] or DP[n]
    #     else:
    #         for n in range(len(s) - 1, -1, -1):
    #             DP[n + 1] = DP[n] and (c == s[n] or c == "?")
    #     DP[0] = DP[0] and c == "*"
    # return 1 if DP[-1] else 0
