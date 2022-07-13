from operator import is_not


arr = tuple(map(int,input().split()))
prefixOdd = [0] * len(arr)
prefixOdd[0] = arr[0]

for i in range(1,len(arr)):
    if i % 2 != 0:
        prefixOdd[i] = prefixOdd[i-1] + arr[i]
    else:
        prefixOdd[i] = prefixOdd[i-1]

print(arr)
print(prefixOdd)
