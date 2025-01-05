""" 
Q4. Merge Overlapping Intervals
Solved
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description

Given a collection of intervals, merge all overlapping intervals.



Problem Constraints

1 <= Total number of intervals <= 100000.



Input Format

First argument is a list of intervals.



Output Format

Return the sorted list of intervals after merging all the overlapping intervals.



Example Input

Input 1:

[1,3],[2,6],[8,10],[15,18]


Example Output

Output 1:

[1,6],[8,10],[15,18]


Example Explanation

Explanation 1:

Merge intervals [1,3] and [2,6] -> [1,6].
so, the required answer after merging is [1,6],[8,10],[15,18].
No more overlapping intervals present.

"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    intervals.sort(key=lambda i: i.start)
    n = len(intervals)
    l = intervals[0].start
    r = intervals[0].end
    res = []

    for i in range(1, n):
        si = intervals[i].start
        ei = intervals[i].end
        if si <= r:
            # overlapping
            r = max(r, ei)
        else:
            # non overlapping
            res.append(Interval(l, r))
            l = si
            r = ei

    res.append(Interval(l, r))

    return res


if __name__ == "__main__":

    a = [1, 3], [2, 6], [8, 10], [15, 18]
    print(merge(a))
