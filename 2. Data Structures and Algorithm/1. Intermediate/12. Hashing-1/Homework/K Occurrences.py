"""
Q1. K Occurrences
Groot has N trees lined up in front of him where the height of the i'th tree is denoted by H[i].
He wants to select some trees to replace his broken branches.
But he wants uniformity in his selection of trees.
So he picks only those trees whose heights have frequency B.
He then sums up the heights that occur B times. (He adds the height only once to the sum and not B times).
But the sum he ended up getting was huge so he prints it modulo 10^9+7.
In case no such cluster exists, Groot becomes sad and prints -1.

Constraints:
1.   1<=N<=100000
2.   1<=B<=N
3.   0<=H[i]<=10^9
Input: Integers N and B and an array C of size N
Output: Sum of all numbers in the array that occur exactly B times.

Example:
Input:
N=5 ,B=2 ,C=[1 2 2 3 3]
Output:
5

Explanation:
There are 3 distinct numbers in the array which are 1,2,3.
Out of these, only 2 and 3 occur twice. Therefore the answer is sum of 2 and 3 which is 5.
"""

# @param A : integer
# @param B : integer
# @param C : list of integers
# @return an integer
def getSumOfKOccurences(B, C):
    #first create a frequency map
    freq = {}
    for i in range(len(C)):
        if C[i] in freq:
            freq[C[i]] +=1
        else:
            freq[C[i]] =1            
    
    # sum of keys whose value is equal to B
    count = 0
    # for key,value in freq.items():
    #     if value == B:
    #         count +=key
    for key in freq:
        if freq[key]==B:
            count +=key
    return count

N=5 
B=2 
C= [1,2,2,3,3]

print(getSumOfKOccurences(B,C))