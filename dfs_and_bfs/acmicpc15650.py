from itertools import combinations
N, M = map(int, input().split())
for c in combinations(list(range(1, N+1)), M):
    print(*c)