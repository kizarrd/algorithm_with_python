from itertools import permutations

N, M = map(int, input().split())
for p in permutations(list(range(1, N+1)), M):
    print(*p)