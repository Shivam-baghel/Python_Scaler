"""
Given an array a, and [s,e] reverse the array for [s,e]  part of the array, where s & e are indices.
Note: s <= e

"""


def reversePart(arr, startIndex, lastIndex):
    while startIndex < lastIndex:
        arr[startIndex], arr[lastIndex] = arr[lastIndex], arr[startIndex]
        startIndex += 1
        lastIndex -= 1

    return arr


a = list(map(int, input().split()))
s, e = map(int, input().split())
print(reversePart(a, s, e))
