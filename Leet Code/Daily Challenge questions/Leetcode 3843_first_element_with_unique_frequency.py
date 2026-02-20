"""
3843. First Element with Unique Frequency

You are given an integer array nums.
Return an integer denoting the first element (scanning from left to right) in nums whose frequency is unique. That is, no other integer appears the same number of times in nums. If there is no such element, return -1.

Example 1:
Input: nums = [20,10,30,30]
Output: 30

Explanation:

20 appears once.
10 appears once.
30 appears twice.
The frequency of 30 is unique because no other integer appears exactly twice.

Example 2:
Input: nums = [20,20,10,30,30,30]
Output: 20

Explanation:

20 appears twice.
10 appears once.
30 appears 3 times.
The frequency of 20, 10, and 30 are unique. The first element that has unique frequency is 20.

Example 3:
Input: nums = [10,10,20,20]
Output: -1

Explanation:

10 appears twice.
20 appears twice.
No element has a unique frequency.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
"""

# idea: count the frequency of each element and then check if the frequency is unique or not by counting the frequency of the frequency. If the frequency of the frequency is 1, then return the element.


# 1st idea using normal counting and then checking the frequency of the frequency.

import collections
from typing import Collection


def first_unique(nums: list[int]) -> int:
    
    num_freq_count: dict[int, int] = {}
    
    for num in nums:
        if num in num_freq_count:
            num_freq_count[num] += 1
        else:
            num_freq_count[num] = 1
            
    freq_count: dict[int,int] = {}
    
    for value in num_freq_count.values():
        if value in freq_count:
            freq_count[value] +=1
        else:
            freq_count[value] = 1
            
    for i in nums:
        freq:int = num_freq_count[i]
        
        if freq_count[freq]==1:
            return i
    
    return -1

# 2nd idea using Counter from collections module to count the frequency of each element and then checking the frequency of the frequency.

def first_unique_using_collections(nums: list[int]) -> int:
    
    freq = collections.Counter(nums)

    freq_count = collections.Counter(freq.values())
    
    for i in nums:
        if freq_count[freq[i]] == 1:
            return i
    
    return -1


if __name__ == "__main__":
    nums = [20,10,30,30]
    print(first_unique_using_collections(nums))
    print(first_unique(nums))