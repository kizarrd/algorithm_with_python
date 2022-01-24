from itertools import combinations

L, C = map(int, input().split())
letters = input().split()
letters.sort()
m = {'a', 'e', 'i', 'o', 'u'}

for combi in combinations(letters, L):
    cnt_m = 0
    for chr in combi:
        if chr in m:
            cnt_m += 1
    if 1 <= cnt_m <= L-2:
        print(''.join(combi))