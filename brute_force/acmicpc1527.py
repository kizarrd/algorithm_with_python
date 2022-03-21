A, B = map(int, input().split())
kmses = []
kms = []
def dfs(n):
    if n == 9:
        return

    kms.append(4)
    kmses.append(int(''.join(map(str, kms))))
    dfs(n+1)
    kms.pop()

    kms.append(7)
    kmses.append(int(''.join(map(str, kms))))
    dfs(n+1)
    kms.pop()
    
dfs(0)

kmses.sort()
cnt = 0
for k in kmses:
    if A<=k<=B:
        cnt += 1
    elif k > B:
        break

print(cnt)