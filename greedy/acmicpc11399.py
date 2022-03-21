import sys
input=sys.stdin.readline
N = int(input())
P = list(map(int, input().split()))
_sum = 0
local_sum = 0
for p in sorted(P):
    local_sum += p
    _sum += local_sum

print(_sum)