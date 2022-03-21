import sys
input=sys.stdin.readline
N = int(input())
P = [0]+list(map(int, input().split()))
d = [0]*(N+1)

for i in range(1, N+1):
    d[i] = P[i]
    for j in range(1, i//2+1):
        d[i] = max(d[i-j]+d[j], d[i])

print(d[N])