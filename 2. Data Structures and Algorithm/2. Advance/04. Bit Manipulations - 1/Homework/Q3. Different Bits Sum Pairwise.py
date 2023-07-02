""" 
Q3. Different Bits Sum Pairwise

We define f(X, Y) as the number of different corresponding bits in the binary representation of X and Y.
For example, f(2, 7) = 2, since the binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.

You are given an array of N positive integers, A1, A2,..., AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.


Problem Constraints
1 <= N <= 105
1 <= A[i] <= 231 - 1

Input Format
The first and only argument of input contains a single integer array A.

Output Format
Return a single integer denoting the sum.

Example Input
Input 1:

 A = [1, 3, 5]
Input 2:

 A = [2, 3]


Example Output
Ouptut 1:
 8
Output 2:
 2

Example Explanation
Explanation 1:
 f(1, 1) + f(1, 3) + f(1, 5) + f(3, 1) + f(3, 3) + f(3, 5) + f(5, 1) + f(5, 3) + f(5, 5) 
 = 0 + 1 + 1 + 1 + 0 + 2 + 1 + 2 + 0 = 8
Explanation 2:
 f(2, 2) + f(2, 3) + f(3, 2) + f(3, 3) = 0 + 1 + 1 + 0 = 2

"""


def cntBits(self, A):
    N=len(A)
    ans=0
    mod=10**9+7

    for i in range(32):
        count1=0
        count0=0
        for j in range(N):

            if (A[j]>>i)&1:
                count1+=1
            else:
                count0+=1

        ans+=(2*count1*count0) % mod


    return ans%mod

    #  #the binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ
    #  010 , whenevr in ith bit  index we encounter 0 or 1
    #  111 , pair it with other elemnts index (which shud be opposite of 0 or 1)
    #  ----
    #  101-->  (1+0+1)=2;   f(2, 7) = 2

     
     
    #  for every x elemnt , there are multiple y elemnts,
    #where at an index like 3=  0    1      1
    #                       5=  1    0      1
    #                       7=  1    1      1
     
    #  0 can paired with 1's or 1 can be paired with 0's in a column
    #  so count no of 0 and no of 1's

    #  contribution for f(x,y) =count1*count0
    #  and for f(y,x) =count1*count0
    #  so total contribution=(2*count1*count0) in a column (or ith bit index)