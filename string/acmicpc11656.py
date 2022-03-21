S = input()
arr = []
for i in range(len(S)):
    arr.append(S[i:])
arr.sort()
for suff in arr:
    print(suff)