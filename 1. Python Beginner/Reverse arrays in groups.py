"""
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size k.
Example:
Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}

Output: 3 2 1 5 4

Explaination : First group consists of elements 1, 2, 3. Second group consists of 4, 5

"""

def reverseInGroups(array, startIndex, size):
    """
    trying to handle but still not done. there is list index out of range error.
    i will check it next day and try to debug it.
    """
    lastIndex = startIndex+size
    if len(array)>=lastIndex:

        while startIndex<lastIndex:
            tempArray = array[startIndex]
            array[startIndex] = array[lastIndex]
            array[lastIndex] = tempArray
            startIndex +=1
            lastIndex -=1
    else:
        lIndex = len(array)
        while startIndex < lIndex:
            tempArray = array[startIndex]
            array[startIndex] = array[lIndex]
            array[lIndex] = tempArray
            startIndex +=1
            lIndex -=1


    return array

inputArray = list(map(int,input("Enter the Array : ").split()))
k = int(input("Enter the size : "))

for index in range(len(inputArray)):
    inputArray = reverseInGroups(inputArray,index,k-1)
    index = index+k

print(inputArray)