""" 
Q1. Merge Intervals

You have a set of non-overlapping intervals. You are given a new interval [start, end], insert this new interval into the set of intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Problem Constraints

0 <= |intervals| <= 105



Input Format

First argument is the vector of intervals

second argument is the new interval to be merged



Output Format

Return the vector of intervals after merging



Example Input

Input 1:

Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
Input 2:

Given intervals [1, 3], [6, 9] insert and merge [2, 6] .


Example Output

Output 1:

 [ [1, 5], [6, 9] ]
Output 2:

 [ [1, 9] ]


Example Explanation

Explanation 1:

(2,5) does not completely merge the given intervals
Explanation 2:

(2,6) completely merges the given intervals

"""


class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        N = len(intervals)
        ans = []
        for i in range(N):

            if (
                newInterval.start > intervals[i].end
            ):  # 1st case distant from starting of new interval
                ans.append(intervals[i])

            elif (
                newInterval.end < intervals[i].start
            ):  # 2nd case distant from ending  of new interval
                ans.append(newInterval)
                k = i
                while k < N:
                    ans.append(intervals[k])
                    k += 1
                return ans

            elif (
                newInterval.end >= intervals[i].start
            ):  # 3rd case end part of new interval is contact with current interval
                newInterval.start = min(
                    intervals[i].start, newInterval.start
                )  # merging it and updating it
                newInterval.end = max(intervals[i].end, newInterval.end)

        ans.append(newInterval)
        return ans
