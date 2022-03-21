import sys
input = sys.stdin.readline

n, k = map(int, input().split())
denominations = [int(input()) for _ in range(n)]
d = [0]*(k+1)
d[0] = 1

for denom in denominations:
    for i in range(denom, k+1):
        d[i] += d[i-denom]

print(d[k])