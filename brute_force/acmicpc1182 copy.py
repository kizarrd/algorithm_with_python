import sys
input=sys.stdin.readline
N, S = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0
def dfs(_sum, i):
    global cnt
    if i == N:
        return
    if _sum+seq[i] == S:
        cnt += 1
        
    dfs(_sum+seq[i], i+1)
    dfs(_sum, i+1)

dfs(0, 0)
print(cnt)