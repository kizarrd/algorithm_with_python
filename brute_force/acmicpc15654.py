from itertools import permutations
N, M = map(int, input().split())
N_numbers = list(map(int, input().split()))
N_numbers.sort()
perms = permutations(N_numbers, M)
for perm in perms:
    print(*perm)