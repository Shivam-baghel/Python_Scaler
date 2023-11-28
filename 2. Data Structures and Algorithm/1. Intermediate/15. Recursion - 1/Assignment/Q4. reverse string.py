""" 
Q4. Print reverse string
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints is now penalty free
Use Hint
Problem Description
Write a recursive function that takes a string, S, as input and prints the characters of S in reverse order.



Problem Constraints
1 <= |s| <= 1000



Input Format
First line of input contains a string S.



Output Format
Print the character of the string S in reverse order.



Example Input
Input 1:

 scaleracademy
Input 2:

 cool


Example Output
Output 1:

 ymedacarelacs
Output 2:

 looc
"""
def reverseString(string:str,eIndex:int):
    
    if eIndex < 0:
        return ""
    
    print(string[eIndex],end="")
    return reverseString(string,eIndex-1)

if __name__ == "__main__":
    st = "cool"
    print(reverseString(st,len(st)-1))