from itertools import combinations_with_replacement as cwr
N, M = map(int, input().split())
combs = cwr(list(range(1, N+1)), M)
for comb in combs:
    print(*comb)