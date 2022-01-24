from itertools import combinations
from collections import deque
while True:
    s = deque(map(int, input().split()))
    if s.popleft() == 0: break

    combs = combinations(s, 6)
    for comb in combs:
        for c in comb:
            print(c, end=' ')
        print()
    print()