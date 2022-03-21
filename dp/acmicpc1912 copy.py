import sys
input=sys.stdin.readline

n = int(input())
d = [0]+list(map(int, input().split()))
for i in range(1, n+1):
    d[i] = max(d[i]+d[i-1], d[i])

print(max(d[1:]))