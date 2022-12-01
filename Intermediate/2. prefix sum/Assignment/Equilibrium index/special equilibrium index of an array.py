"""
Q2. Count ways to make sum of odd and even indexed elements equal by removing an array element (asked by google in their interviews.)

Problem Description
Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element 
from these indices makes the sum of even-indexed and odd-indexed array elements equal.

Problem Constraints                     |   Input Format
1 <= n <= 105                           |   First argument contains an array A of integers of size N
-105 <= A[i] <= 105                     |

Output Format
Return the count of array indices such that removing an element from these indices 
makes the sum of even-indexed and odd-indexed array elements equal.

Example Input
Input 1:
A=[2, 1, 6, 4]
Input 2:
A=[1, 1, 1]

Example Output
Output 1:
1
Output 2:
3

Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
Therefore, the required output is 1. 
Explanation 2:
Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Therefore, the required output is 3.

"""

def sumOfEven(evenArray:list,startIndex:int,endIndex:int):
    """this array return the sumation of odd index's of the array excluding the given index.

    Args:
        oddArray (list): prefix odd sum array.
        startIndex (int): starting index
        endIndex (int): ending index

    Returns:
        Integer: returns the outpupt
    """
    
    if startIndex > 0:
        return evenArray[endIndex-1]-evenArray[startIndex]
    else:
        return evenArray[endIndex-1]
    
def sumOfOdd(oddArray:list,startIndex:int,endIndex:int):
    """this array return the sumation of odd index's of the array excluding the given index.

    Args:
        oddArray (list): prefix odd sum array.
        startIndex (int): starting index
        endIndex (int): ending index

    Returns:
        Integer: returns the output 
    """
    
    if startIndex > 0:
        return oddArray[endIndex-1]-oddArray[startIndex]
    else:
        return oddArray[endIndex-1]
    
def specialEquibliriumIndex(array:list):
    """ This function will for every index. If that index is special index then the count will increase.

    Args:
        array (list): list of intergers.
    Return:
        return: the count of special index's present in the given list of integers.
        
    """
    
    length_of_Array = len(array)
    
    # first create prefix even sum array.
    
    prefix_even_sum = [0]*length_of_Array
    prefix_even_sum[0] = array[0]
    
    for index in range(1,length_of_Array):
        # Bit manipulation way to check if value is even or odd.
        if index&1 == 0:
            prefix_even_sum[index] = prefix_even_sum[index-1] + array[index]
        else:
            prefix_even_sum[index] = prefix_even_sum[index-1]
            
    # create prefix odd sum array. 
    
    prefix_odd_sum = [0] * length_of_Array
    prefix_odd_sum[0] = array[0]
    
    for index in range(1,length_of_Array):
        # Bit manipulation way to check jif value is even or odd.
        if index & 1 == 1:
            prefix_odd_sum[index] = prefix_odd_sum[index-1] + array[index]
        else:
            prefix_odd_sum[index] = prefix_odd_sum[index-1]
            
    
    # create a loop for checking if the paricular index is specilised index or not.
    count = 0
    for index,value in enumerate(array):
        
        # check if a index is a special index or not.
        sumEven = sumOfEven(prefix_even_sum,0,index)+sumOfOdd(prefix_even_sum,index,length_of_Array)
        sumOdd = sumOfOdd(prefix_odd_sum,0,index)+sumOfEven(prefix_odd_sum,index,length_of_Array)
        
        if sumEven == sumOdd:
            count +=1
    
    return count

A=[2, 1, 6, 4]
print(specialEquibliriumIndex(A))