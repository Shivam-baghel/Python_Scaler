# A = [["53..7...."], ["6..195..."], [".98....6."], ["8...6...3"], ["4..8.3..1"], ["7...2...6"], [".6....28."], ["...419..5"], ["....8..79"]]
# arr = []
# def sub(n):
#     if n == '.':
#         return 0
#     else:
#         return int(n)
    
    
# for i in range(len(A)):
#     val = [c for c in A[i]]
#     value = list(val)
#     print(value)
#     for i in val:
#         print(i)
#     # value = [0 if i =='.' else int(i) for i in val]
#     # print(value)
#     sol = []
#     # using loop
#     # for i in range(0, len(val)):
#     #     if val[i] == '.':
#     #         val[i]=int(0)
#     #     else:
    
#     #         val[i] = int(val[i])
#     #     sol.append(val[i])

#     # arr.append(sol)    
# print(arr)


# a = "531....7.."
# val = list(a)
# print(val)

A = [["53..7...."], ["6..195..."], [".98....6."], ["8...6...3"], ["4..8.3..1"], ["7...2...6"], [".6....28."], ["...419..5"], ["....8..79"]]
cur = []
for i in A:
    print(i)
    sol = []
    for j in i:
        val = list(j)
        sol.append([0 if i =='.' else int(i) for i in val])
    cur.append(sol)
print(cur)