arr = list(map(int,input().split()))        # accepting the array.

prefixEven = [0] * len(arr)     # creating a new dirrerent array for prefixEven array.
prefixEven[0] = arr[0]          # makeing the first element of the prefixEven array equal to the first element of the array.

for i in range(1,len(arr)):
    if i % 2 == 0:          # populating the prefixEven array with even index values only.
        prefixEven[i] = prefixEven[i-1] + arr[i]
    else:
        prefixEven[i] = prefixEven[i-1]

print(arr)
print(prefixEven)           #p rinting the prefixEven values.
