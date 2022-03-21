# Time limit exceeded
from itertools import combinations
from bisect import bisect_right
N = int(input())
S = list(map(int, input().split()))
S.sort()
i = 1
while True:
    j = bisect_right(S, i)
    combs = []
    for k in range(j, 0, -1):
        combs+=list(map(sum, combinations(S[:j], k)))
    if i not in combs:
        print(i)
        exit()
    i+=1