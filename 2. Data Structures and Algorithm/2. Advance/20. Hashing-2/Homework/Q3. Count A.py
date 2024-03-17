""" 
Q3. Count A
You are given a string A. Find the number of substrings that start and end with 'a'.

Problem Constraints
1 <= |A| <= 105

The string will have only lowercase English letters.

Input Format
Given the only argument is a String A.

Output Format
Return number of substrings that start and end with 'a'.

Example Input
Input 1:

 A = "aab"
Input 2:

 A = "bcbc"


Example Output
Output 1:

 3
Output 2:

 0


Example Explanation
Explanation 1:

 Substrings that start and end with 'a' are:
    1. "a"
    2. "aa"
    3. "a"
Explanation 2:

 There are no substrings that start and end with 'a'.
"""


def countA(a: str):

    count = 0

    for i in a:

        if i == "a":
            count += 1

    return (count * (count + 1)) // 2


if __name__ == "__main__":
    string = "aab"
    print(countA(string))
