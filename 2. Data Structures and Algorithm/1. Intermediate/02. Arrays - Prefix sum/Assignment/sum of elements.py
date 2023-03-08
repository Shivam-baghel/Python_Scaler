"""
Given N array elements and Q queries on same array for each query, start and end index would be provided.
calculate the sum of elements between start and end index.

"""
def sumOfElements(A, startIndex, lastIndex):

    sumOfElements = 0       # this variable will store sum of elements.

    for i in range(startIndex,lastIndex+1):     # going from start index to last index of the array.

        sumOfElements = sumOfElements + A[i]        # extracting the elements of the array one by one and adding it to the sumOfElements variable.

    print(sumOfElements)    # Printing the sum.

arr = tuple(map(int,input().split()))       # Accepting the array

queries = int(input())      # accepting the no. of queries

while queries > 0 :
    queries -= 1        # decreasing the queries count otherwise loop will go for infinte.

    startIndex,lastIndex = map(int,input().split())         # accepting the start and end Index queries.
    sumOfElements(arr, startIndex, lastIndex)


"""
The time complexity of this program would be O(n^2) bcause of the 2 nested loops
The space complexiy of this program would be O(n) because we are accepting an array.

"""

