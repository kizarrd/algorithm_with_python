from itertools import combinations, permutations

k = int(input())
inequation = input().split()
integers = list(range(10))
numbers_combinations = combinations(integers, k+1)

def satisfies_inequation(perm):
    for i in range(k):
        if inequation[i] == '>':
            if not(perm[i]>perm[i+1]):
                return False
        else: # elif inequation[i] == '<'
            if not(perm[i]<perm[i+1]):
                return False
    return True

_min = '9'*(k+1)
_max = '0'*(k+1)
for numbers in numbers_combinations:
    perms = permutations(numbers, k+1)
    for perm in perms:
        if satisfies_inequation(perm):
            number_str = ''.join(map(str, perm))
            _min = min(_min, number_str)
            _max = max(_max, number_str)

print(_max)
print(_min)