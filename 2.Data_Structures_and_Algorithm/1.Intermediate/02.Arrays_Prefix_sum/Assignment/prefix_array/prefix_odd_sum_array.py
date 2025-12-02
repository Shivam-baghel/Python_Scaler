# arr = tuple(map(int ,input().split()))       # accepting the array
def prefixOddSum(arr):
    # creating a new different array for prefixOdd array

    prefixOdd = [0] * len(arr)

    # make the first element of the prefixOdd array equal to the 0. As 0th index is even and we don't have any previous element which we can use to determine 0th index value.

    prefixOdd[0] = 0

    for i in range(1, len(arr)):
        # populating the prefixodd array with odd index values only.

        if i % 2 != 0:
            prefixOdd[i] = prefixOdd[i - 1] + arr[i]

        else:
            prefixOdd[i] = prefixOdd[i - 1]

    print(arr)
    print(prefixOdd)  # printing the prefixOdd array


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    prefixOddSum(array)
