from itertools import combinations

L, C = map(int, input().split())
letters = input().split()
letters.sort()
vowels = {'a', 'e', 'i', 'o', 'u'}
n_vowel_limit = L-2
combs = combinations(letters, L)
for comb in combs:
    vowel_cnt = 0
    for c in comb:
        if c in vowels:
            vowel_cnt += 1
    if 0 < vowel_cnt <= n_vowel_limit:
        print(''.join(comb))