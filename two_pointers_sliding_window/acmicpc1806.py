import sys
input=sys.stdin.readline
N, S = map(int, input().split())
seq = list(map(int, input().split()))

_sum = 0
min_len = N+1
left, right = 0, 0
while right < len(seq):
    if _sum < S:
        _sum += seq[right]
        right += 1
    if _sum >= S:
        while left <= right and _sum >= S:
            if right-left < min_len:
                min_len = right-left
            if left+1 <= right:
                _sum -= seq[left]
                left += 1

if min_len < N+1:
    print(min_len)
else:
    print(0)