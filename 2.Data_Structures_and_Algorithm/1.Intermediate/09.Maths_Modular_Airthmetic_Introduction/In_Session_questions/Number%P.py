"""
Given 1 number in array of size N. Calculate number % p?
Each digit of the number is given in array[i]
Ex : no. = 7869 array arr=[7,8,6,9]
constraints:
N=size of the array and no. of digits in th number <= 10^5
p<=10^5
0<=arr[i]<=9
"""


def arrayMod(arr: tuple, p: int):
    lengthOfArray = len(arr)
    result = 0
    x = 1
    for i in range(lengthOfArray - 1, -1, -1):
        digit = arr[i] % p
        result = (result + (digit * x) % p) % p
        x = (x * 10) % p

    return result


arr = tuple(map(int, input().split()))
p = int(input())
print(arrayMod(arr, p))
