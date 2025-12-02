""" 
Q1. Permutations of A in B
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints is now penalty free
Use Hint
Problem Description
You are given two strings, A and B, of size N and M, respectively.

You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.



Problem Constraints
1 <= N < M <= 105



Input Format
Given two arguments, A and B of type String.



Output Format
Return a single integer, i.e., number of permutations of A present in B as a substring.



Example Input
Input 1:

 A = "abc"
 B = "abcbacabc"
Input 2:

 A = "aca"
 B = "acaa"


Example Output
Output 1:

 5
Output 2:

 2


Example Explanation
Explanation 1:

 Permutations of A that are present in B as substring are:
    1. abc
    2. cba
    3. bac
    4. cab
    5. abc
    So ans is 5.
Explanation 2:

 Permutations of A that are present in B as substring are:
    1. aca
    2. caa 
"""


# create a hashmap of A
# create a hashmap of window of length of A from B starting elemnts
# start moving the window , by removing starting index  and add upcoming index in window hashmap
# whnever hashmap of both matches , that means current  window is permutation of A

def hashmap(X): # function for making a hashmap or dictionary
    dictX={}
    for i in X:
        if i not in dictX:
            dictX[i]=0
        dictX[i]+=1
    return dictX


def permutationsOfAInB( A, B):
    N=len(A)
    M=len(B)
    ans=0
    dictA=hashmap(A)  # create a hashmap of A
    X=""
    for i in range(0,N):
        X+=B[i]
    dictX=hashmap(X) # create a hashmap of moving window

    i=0 # window index
    j=N-1

    while j<M:              
        if dictX==dictA: # if hashmap of both matches
            ans+=1         # that means that window is permutation of A

        dictX[B[i]]-=1 # remove starting index in window hashmap
        if dictX[B[i]]==0:
            del dictX[B[i]]
        i+=1

        j+=1   # add upcoming index in window hashmap
        if j==M:
            break
        if B[j] in dictX:
            dictX[B[j]]+=1
        else:
            dictX[B[j]]=1            
        
    return ans