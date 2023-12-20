""" 
Problem
Chef embarks on a journey starting from a town named S, containing a string of 8 uppercase English alphabets. His objective is to reach the destination known as CODETOWN.

If Chef is currently in town T1, then, with each move, Chef can transition to another town named T2, provided that either:

T2 is derived from T1 by replacing a consonant with another consonant, or
T2 is derived from T1 by replacing a vowel with another vowel.
Find whether Chef can reach CODETOWN in any number of moves.
Note that in the english alphabet, letters A, E, I, O, and U are considered as vowels and rest are considered as consonants.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a string S, of length 8 consisting of uppercase english alphabets.

Output Format
For each test case, output on a new line, YES, if Chef can reach CODETOWN, and NO otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

S consists of uppercase english alphabets.
Sample 1:
Input
Output
3
YAPETOWN
CODECHEF
CODETOWN
YES
NO
YES
Explanation:
Test case 
1
1: Chef can reach to CODETOWN in the following way: YAPETOWN 
→
→ CAPETOWN 
→
→ COPETOWN 
→
→ CODETOWN.

Test case 
2
2: It can be shown that Chef would not be able to reach CODETOWN.

Test case 
3
3: Chef is already in CODETOWN.
"""
check = {'A','I','E','O','U'}
code = "CODETOWN"

check_list = [0]*len(code)
for i in range(len(code)):
    
    if code[i] in check:
        check_list[i] = 1

t = int(input())
while t > 0:
    
    a_string = input()
    check_string = [0]*8
    for i in range(8):
        if a_string[i] in check:
            check_string[i] = 1
    
    # Check if the lists are identical
    result = all(x == y for x, y in zip(check_list, check_string))
    if result:
        print("Yes")
    else:
        print("NO")
    
    t -= 1