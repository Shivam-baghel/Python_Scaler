"""
Q3. Colorful Number
Given a number A, find if it is COLORFUL number or not.
If number A is a COLORFUL number return 1 else, return 0.

What is a COLORFUL Number:
A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.

Problem Constraints
1 <= A <= 2 * 109

Input Format
The first and only argument is an integer A.

Output Format
Return 1 if integer A is COLORFUL else return 0.

Example Input
Input 1:
 A = 23
Input 2:
 A = 236

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 Possible Sub-sequences: [2, 3, 23] where
 2 -> 2 
 3 -> 3
 23 -> 6  (product of digits)
 This number is a COLORFUL number since product of every digit of a sub-sequence are different. 
Explanation 2:
 Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where
 2 -> 2 
 3 -> 3
 6 -> 6
 23 -> 6  (product of digits)
 36 -> 18  (product of digits)
 236 -> 36  (product of digits)
 This number is not a COLORFUL number since the product sequence 23  and sequence 6 is same.
"""

# @param A : integer
# @return an integer
def colorful(A):
    # hashset = set()
    # a = str(A)
    
    # for i in range(len(a)):
    #     product =1 
    #     for j in range(i,len(a)):
    #         product = product* int(a[j])
    #         if product in hashset:
    #             return 0
    #         else:
    #             hashset.add(product)
    
    # return 1

    # or second way
    hashset = set()
    a = str(A)
    
    for i in range(len(a)):
        product =1 
        for j in range(i,len(a)):
            product = product* int(a[j])
            hashset.add(product)

    #Total no of sub array present in an array:
    n = ((len(a)+1)*len(a))//2
    if len(hashset)==n:
        return 1
    else:
        return 0

A=123
print(colorful(A))