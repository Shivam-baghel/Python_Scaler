"""
Given N array elements and Q queries on same array for each query, start and end index would be provided.
calculate the sum of elements between start and end index.

we have already done this question in sum of elements. Here we are creating optamized code for the same.
we will try solve it by prefix sum.

general form:
to get the sum from prefix array from index [i,j]

    if i > 0, pf[j] - pf[i-1]  ,   pf means prefix array.
    if i == 0, pf[j]


"""


def sumOfElements(A, startIndex, lastIndex):
    sumOfElements = 0  # this variable will store sum of elements.

    if startIndex > 0:  # we are using prefix sum formula.

        sumOfElements = A[lastIndex] - A[startIndex - 1]

    else:

        sumOfElements = A[lastIndex]

    print(sumOfElements)  # Printing the sum.


arr = tuple(map(int, input().split()))  # Accepting the array

prefixArray = [0] * len(arr)  # creating the prefix array.
prefixArray[0] = arr[0]
for i in range(1, len(arr)):
    prefixArray[i] = prefixArray[i - 1] + arr[i]

queries = int(input())  # accepting the no. of queries

while queries > 0:
    queries -= 1  # decreasing the queries count otherwise loop will go for infinte.

    startIndex, lastIndex = map(int, input().split())  # accepting the start and end Index queries.
    sumOfElements(prefixArray, startIndex, lastIndex)

"""
The time complexity of this program would be O(2n) bcause of the 2 loops
The space complexiy of this program would be O(2n) because we are accepting an array creating a different array again.

"""
