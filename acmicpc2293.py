import sys
input = sys.stdin.readline
n, k = map(int, input().split())
denominations = [int(input()) for _ in range(n)]

cnt = 0
def recursive(p, val):
    global cnt
    if val == k:
        cnt += 1
        return
    if p == len(denominations) or val > k:
        return
    
    for i in range(k//denominations[p]+1):
        nv = denominations[p]*i + val
        recursive(p+1, nv)

recursive(0, 0)

print(cnt)