


arr = tuple(map(int,input().split()))       # accepting the array
prefixOdd = [0] * len(arr)          # creating a new different array for prefixOdd array
prefixOdd[0] = arr[0]           # make the first element of the prefixOdd array equal to the first element of the array.

for i in range(1,len(arr)):
    if i % 2 != 0:              # populating the prefixodd array with odd index values only.
        prefixOdd[i] = prefixOdd[i-1] + arr[i]
    else:
        prefixOdd[i] = prefixOdd[i-1]

print(arr)
print(prefixOdd)            # printing the prefixOdd array
