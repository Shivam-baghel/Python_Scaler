""" 
Q2. Minimum Swaps

Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.

Problem Constraints
1 <= length of the array <= 100000
-109 <= A[i], B <= 109

Input Format

The first argument given is the integer array A.
The second argument given is the integer B.

Output Format

Return the minimum number of swaps.

Example Input

Input 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 B = 8
Input 2:

 A = [5, 17, 100, 11]
 B = 20


Example Output

Output 1:

 2
Output 2:

 1
"""

""" 
idea is  to find the total numbers which are less than B. with these number we will get idea of a window size. then take that
windows size and check how many number are present inside that window which are less than B lets call those numbers good
numbers rest of the numbers in that window are bad no. move that window along every index of the array and find good and
bad no. present in each window of the array using window sliding technique. Our goal is to find the window having 0 bad
numbers or mininum bad numbers across all the windows in an array. and return the minimum bad numbers as the answer.
"""


def minimum_swap(A: list, B: int):
    arr = A
    length_of_arr = len(arr)

    count_num_to_swap = 0  # will give total good numbers in the array and the window size.
    for i in arr:
        if i <= B:
            count_num_to_swap += 1

    if count_num_to_swap <= 1:
        return 0
    else:
        left, right, x = 0, 0, 0  # x represent the bad numbers present inside the window
        while right < count_num_to_swap:
            if arr[right] > B:
                x += 1
            right += 1

        ans = x
        while right < length_of_arr:
            if arr[right] > B:
                x += 1
            if arr[left] > B:
                x -= 1
            ans = min(ans, x)
            left += 1
            right += 1

    return ans


if __name__ == '__main__':
    A = [1, 12, 10, 3, 14, 10, 5]
    B = 8
    print(minimum_swap(A, B))
