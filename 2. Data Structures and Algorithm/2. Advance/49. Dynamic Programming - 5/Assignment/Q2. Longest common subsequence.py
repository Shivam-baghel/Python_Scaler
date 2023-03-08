""" 
Q2. Longest Common Subsequence
Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous), which is common in both the strings.
You need to return the length of such longest common subsequence.

Problem Constraints
1 <= Length of A, B <= 1005

Input Format
First argument is a string A.
Second argument is a string B.

Output Format
Return an integer denoting the length of the longest common subsequence.

Example Input
Input 1:
 A = "abbcdgf"
 B = "bbadcgf"
Input 2:
 A = "aaaaaa"
 B = "ababab"

Example Output
Output 1:
 5
Output 2:
 3

Example Explanation
Explanation 1:
 The longest common subsequence is "bbcgf", which has a length of 5.
Explanation 2:
 The longest common subsequence is "aaa", which has a length of 3.
"""
def Get_Long_Common_Length(string_1,string_2):
    length_of_str1 = len(string_1)
    length_of_str2 = len(string_2)
    dp = []
    for i in range(length_of_str1):
        col = []
        for j in range(length_of_str2):
            col.append(-1)
        dp.append(col)
    
    def LongestCommonSubsequence(string_1:str,string_2:str,str1_p:int,str2_p:int):
        if (str1_p < 0 or str2_p < 0 ):     # if any one of string is empty , there is nothing in common.
            return 0
        
        if dp[str1_p][str2_p] == -1:    #First time calling of that particular cell in dp matrix.
            
            if string_1[str1_p] == string_2[str2_p]:    # that particular index of both string matches.
                dp[str1_p][str2_p] = LongestCommonSubsequence(string_1,string_2,str1_p-1,str2_p-1) + 1
            else:
                dp[str1_p][str2_p] = max(LongestCommonSubsequence(string_1,string_2,str1_p-1,str2_p),LongestCommonSubsequence(string_1,string_2,str1_p,str2_p-1))
                
        return dp[str1_p][str2_p]
    
    return LongestCommonSubsequence(string_1,string_2,length_of_str1-1,length_of_str2-1)
def main():
    A = "abbcdgf"
    B = "bbadcgf"
    print(Get_Long_Common_Length(A,B))
    return

if __name__ == "__main__":
    main()