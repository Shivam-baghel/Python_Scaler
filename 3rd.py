def ques(arr:list,k):
    r = len(arr)
    if r == 1:
        if arr[0]==1:
            return 1
        else:
            return 0

    l = r-(k-1)-1
    c=0
    ans=0
    for i in range(l,r):
        if arr[i]==1:
            c = c+1
    
    for j in range(c,0,-1):
        ans = ans+j 
    
    for k in range(l):
        if arr[k]==1:
            ans = ans+ 1
    
    return ans

a = [1]
k=1
print(ques(a,k))