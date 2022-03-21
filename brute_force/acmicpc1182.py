from itertools import combinations
import sys
input=sys.stdin.readline
N, S = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0

for i in range(1, N+1):
    combs = combinations(seq, i)
    for combi in combs:
        if sum(combi) == S:
            cnt += 1

print(cnt)