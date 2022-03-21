from itertools import product
N, M = map(int, input().split())

for p in product(list(range(1, N+1)), repeat=M):
    print(*p)