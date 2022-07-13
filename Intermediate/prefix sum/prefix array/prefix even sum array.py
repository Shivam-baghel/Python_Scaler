arr = list(map(int,input().split()))

prefixEven = [0] * len(arr)
prefixEven[0] = arr[0]

for i in range(1,len(arr)):
    if i % 2 == 0:
        prefixEven[i] = prefixEven[i-1] + arr[i]
    else:
        prefixEven[i] = prefixEven[i-1]

print(arr)
print(prefixEven)
