""" 
Q1. Length of Longest Sequence.
Given an array having N elements. find the length of the longest sub-Sequence which can be re-arranged in a strictly
increasing by 1 order.

Note : Index elements does not have to be continous.

Example :

Input 1 :
array = [-1,8,5,3,10,2,4,9]

Output 1 :
ans = 4 [2,3,4,5]

"""

# Idea 1 is to sort the array. then compare the adjacent values to get the length.

def longest_seq1(arr:list):
    len_arr = len(arr)
    # sort the array
    arr.sort()

    # let's comapare the adjacent values in array to get the max length
    
    ans = 0
    i = 1
    while (i < len_arr):
        
        length = 1
        while i < len_arr:
            if arr[i]-arr[i-1] == 1:
                length += 1
                i += 1
            elif arr[i]-arr[i-1] == 0:
                i += 1
            else:
                break
        
        i += 1   
        ans = max(ans,length)
    
    return ans

if __name__ == "__main__":
    a=[-1,8,5,3,10,2,4,9]
    print(longest_seq1(a))