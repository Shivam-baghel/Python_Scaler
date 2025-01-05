""" 
Q2. Aggressive cows
Solved
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description

Farmer John has built a new long barn with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall and an integer B which represents the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?



Problem Constraints

2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.



Output Format

Return the largest minimum distance possible among the cows.



Example Input

Input 1:

A = [1, 2, 3, 4, 5]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 John can assign the stalls at location 1, 3 and 5 to the 3 cows respectively. So the minimum distance will be 2.
Explanation 2:

 The minimum distance will be 1.
 
"""

#     def solve(self, A, B):
#         # A.sort()
#         # length = len(A)
#         # #low is minimum adjacent distance between A
#         # low = A[0]
#         # for i in range(length-1):
#         #     if low > abs(A[i]-A[i+1]):
#         #         low = abs(A[i]-A[i+1])

#         # high = A[length-1]-A[0]
#         # ans = high

#         # while(low <= high):
#         #     mid = (low+high)//2

#         #     if self.checkfun(length,B,A,mid):
#         #         ans = mid
#         #         low = mid+1
#         #     else:
#         #         high = mid-1

#         # return ans%10000007

#         N = len(stalls)
#         low = 1
#         high = stalls[N-1] - stalls[0]
#         ans = 0

#         while low <= high:
#             mid  = low + (high - low) // 2
#             if self.check(stalls,mid,k):
#                 ans = mid
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return ans

#         def check(self,stalls,mid,total_cow):
#         last_placed_cow = stalls[0]
#         count_cow = 1

#         for i in range(1,len(stalls)):
#             if stalls[i] - last_placed_cow >= mid:
#                 last_placed_cow = stalls[i]
#                 count_cow += 1

#             if count_cow == total_cow:
#                 return True
#         return False


#     def solve(self, A, B):
#         A.sort()
#         res = self.aggressiveCows(A,B)

#         return res


def checkCowsPlaced(A, mid, B):
    cowsPlaced = A[0]
    cowsCount = 1

    for i in range(len(A)):
        if A[i] - cowsPlaced >= mid:
            cowsCount += 1
            cowsPlaced = A[i]

            if cowsCount == B:
                return True

    return False


def aggresssiveCows(A, B):
    A.sort()
    start = 1
    end = A[-1] - A[0]
    result = 0

    while start <= end:
        mid = (start + end) >> 1
        if checkCowsPlaced(A, mid, B):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result
