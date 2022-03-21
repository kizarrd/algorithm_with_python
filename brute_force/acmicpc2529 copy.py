from itertools import permutations

k = int(input())
inequation = input().split()

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
perms = permutations(list(range(10)), k+1)
for perm in perms:
    if satisfies_inequation(perm):
        number_str = ''.join(map(str, perm))
        _min = min(_min, number_str)
        _max = max(_max, number_str)

print(_max)
print(_min)