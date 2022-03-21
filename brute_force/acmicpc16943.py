from itertools import permutations
A, B = input().split()
B = int(B)
Cs = permutations(list(A), len(A))
Cs = list(int(''.join(x)) for x in Cs if x[0] != '0')
Cs.sort()

C = -1
for candidate in Cs:
    if candidate >= B:
        break
    C = candidate

print(C)