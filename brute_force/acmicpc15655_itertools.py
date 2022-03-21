from itertools import combinations
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
combs = combinations(numbers, M)
for comb in combs:
    print(*comb)