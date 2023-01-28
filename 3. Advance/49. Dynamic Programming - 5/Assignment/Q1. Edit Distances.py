""" 
Q1. Edit Distance
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Problem Constraints
1 <= length(A), length(B) <= 450

Input Format
The first argument of input contains a string, A.
The second argument of input contains a string, B.

Output Format
Return an integer, representing the minimum number of steps required.

Example Input
Input 1:
 A = "abad"
 B = "abac"
Input 2:
 A = "Anshuman"
 B = "Antihuman
 
Example Output
Output 1:
 1
Output 2:
 2

Example Explanation
Exlanation 1:
 A = "abad" and B = "abac"
 After applying operation: Replace d with c. We get A = B.
 
Explanation 2:
 A = "Anshuman" and B = "Antihuman"
 After applying operations: Replace s with t and insert i before h. We get A = B
"""
def Get_Distance(String_1:str,String_2:str):
    length_of_str1 = len(String_1)
    length_of_str2 = len(String_2)
    
    dp = []
    for i in range(length_of_str1):
        col = []
        for j in range(length_of_str2):
            col.append(-1)
        dp.append(col)
    
    def Edit_distance(s1:str,s2:str,s1_p:int,s2_p:int):
        if s1_p < 0 and s2_p < 0:   # if s1 and s2 both are empty stirngs.
            return 0
        
def main():
    return
if __name__ == "__main__":
    main()