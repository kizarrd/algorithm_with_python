from itertools import combinations
dwarfs = [int(input()) for _ in range(9)]
for c in combinations(dwarfs, 7):
    if sum(c) == 100:
        print(*sorted(c), sep='\n')
        exit(0)