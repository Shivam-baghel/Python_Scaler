""" 
Given N distinct elements, Print K smallest elements in array k<N, in increasing order.
"""

import heapq as heap
import numpy as np

def kthSmallestElement(array:list,k:int):
    arrayList = []
    
    for i in range(k):
        heap.heappush(arrayList,(-1*array[i]))
    
    lengthOfArray = len(array)
    
    for j in range(k,lengthOfArray):
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