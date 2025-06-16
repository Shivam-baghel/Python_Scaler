# accepting the array.

# arr = list(map(int, input().split()))
def prefixEvenSum(arr):
    prefixEven = [0] * len(arr)  # creating a new dirrerent array for prefixEven array.

    # makeing the first element of the prefixEven array equal to the first element of the array.
    prefixEven[0] = arr[0]

    for i in range(1, len(arr)):
        if i % 2 == 0:  # populating the prefixEven array with even index values only.
            prefixEven[i] = prefixEven[i - 1] + arr[i]
        else:
            prefixEven[i] = prefixEven[i - 1]

    print(arr)

    # printing the prefixEven values.

    print(prefixEven)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    prefixEvenSum(array)
