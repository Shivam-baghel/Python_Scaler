"""
Q1. Common Elements
Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.

NOTE:Each element in the result should appear as many times as it appears in both arrays.The result can be in any order.

Problem Constraints
1 <= N, M <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A of size N.
Second argument is an integer array B of size M.

Output Format
Return an integer array denoting the common elements.

Example Input
Input 1:
A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
Input 2:
A = [2, 1, 4, 10]
B = [3, 6, 2, 10, 10]

Example Output
Output 1:
[1, 2, 2]
Output 2:
[2, 10]

Example Explanation
Explanation 1:
Elements (1, 2, 2) appears in both the array. Note 2 appears twice in both the array.
Explantion 2:
Elements (2, 10) appears in both the array.

"""
def commonElement( A, B):

    # create a frequency Map for list A
    freqMapforA = {}
    for element in A:
        if element in freqMapforA:
            freqMapforA[element] +=1
        else:
            freqMapforA[element] = 1
    
    # create a frequency Map for list B
    freqMapforB = {}
    for element in B:
        if element in freqMapforB:
            freqMapforB[element] +=1
        else:
            freqMapforB[element] =1
    
    # add list A & list B to a set
    hashset = set()
    hashset.update(A)
    hashset.update(B)

    # to store answer
    ans = []

    # Iterate on hashset
    for item in hashset:
        # check if item is in frequency Map of list A. if not a = 0
        if item in freqMapforA:
            a = freqMapforA[item]
        else:
            a = 0

        # check if item is in frequency Map of list B. if not b = 0
        if item in freqMapforB:
            b = freqMapforB[item]
        else:
            b = 0
        
        # if a and b either of them are not equal to 0. find minimum between them and append to list.
        if a != 0 and b != 0 :
            m = min(a,b)
            # append the item to list ans, mini is minimum between list a and b.
            # item will appear minimum of m times on list a and b.
            ans.extend([item]*m)
        else:
            continue
    
    return ans

A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
print(commonElement(A,B))