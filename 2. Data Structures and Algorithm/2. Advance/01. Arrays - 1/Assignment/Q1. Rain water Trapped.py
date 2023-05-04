""" 
Q1. Rain Water Trapped
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Problem Constraints
1 <= |A| <= 100000

Input Format
First and only argument is the vector A

Output Format
Return one integer, the answer to the question

Example Input

Input 1:
A = [0, 1, 0, 2]

Input 2:
A = [1, 2]

Example Output
Output 1:
1
Output 2:
0

Example Explanation

Explanation 1:
1 unit is trapped on top of the 3rd element.

Explanation 2:
No water is trapped.
"""
# Idea 1 using recusion This is from the book

def trap(A):

    # Finds the index with maximum height.
    max_h = A.index(max(A))

    #Assume heights [-1] is maximum hieght.
    def trappingWaterTillEnd(A):
        partialSum, highestLevelSeen = 0, float('-inf')
        for h in A:
            if h >=  highestLevelSeen:
                highestLevelSeen = h 
            else:
                partialSum += highestLevelSeen - h 
        
        return partialSum
    
    return (trappingWaterTillEnd(A[:max_h]) + trappingWaterTillEnd(reversed(A[max_h+1:])))

# idea 2 taught in calss.
    # for a current height check the max height on the left and the right side of the current height.
    # find out which is the minimum of those two height and minus that with current height. you will get water stored on the current building and store the value in new list caller water.
    # find the water value for each index in the list building hieght. return the addition of the entire water.

def water(array):
    return