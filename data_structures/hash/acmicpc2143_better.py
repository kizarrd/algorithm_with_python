from collections import defaultdict
import sys
input=sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sums_A = defaultdict(int)

for l in range(n):
    _sum = 0
    for r in range(l, n):
        _sum += A[r]
        sums_A[_sum] += 1

cnt = 0
for l in range(m):
    _sum = 0
    for r in range(l, m):
        _sum += B[r]
        cnt += sums_A[T-_sum]

print(cnt)