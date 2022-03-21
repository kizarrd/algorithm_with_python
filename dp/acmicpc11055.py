import sys
input=sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
# d[i] = max sum of the subsequence including A[i]
d = [0]*N
_max = 0
for i in range(0, N):
    d[i] = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            d[i] = max(d[i], A[i]+d[j])
    _max = max(_max, d[i])

print(_max)