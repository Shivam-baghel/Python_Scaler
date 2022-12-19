""" 
Given N distinct elements, Print K smallest elements in array k<N, in increasing order.
"""

import heapq as heap
import numpy as np

def kthSmallestElement(array:list,k:int):
    arrayList = []
    # Push  K elements in max Heap.
    # (heapq does not has any implementation for max heap. so we are useing min heap did some modification on data so that min behaves like max Heap)
    for i in range(k):
        heap.heappush(arrayList,(-1*array[i]))
    
    lengthOfArray = len(array)
    
    for j in range(k,lengthOfArray):
        # if element is less than values present in heap.
            #- push the element in heap and pop the max element in heap.
        if array[j] < (-1 * arrayList[0]):
            heap.heappush(arrayList,(-1 *array[j]))
            heap.heappop(arrayList)

    arr = np.array(arrayList)
    ar = arr*-1
    # we can also use ar.reverse() if we had not used numpy.
    # flip function is used to reverse the numpy array.
    return np.flip(ar)

A =[8,3,10,4,11,2,7,5,14,1]
print(kthSmallestElement(A,4))
