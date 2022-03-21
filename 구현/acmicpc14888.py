from itertools import permutations
import math
N = int(input())
A = list(map(int, input().split()))
n_operators = list(map(int, input().split()))
operators = []
for i, n in enumerate(n_operators):
    for _ in range(n):
        operators.append(i)

permutations_of_ops = set(permutations(operators, N-1))

def compute(a, b, op):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    elif op == 3:
        if a < 0:
            return -((-a)//b)
        return a//b

_max = -math.inf
_min = math.inf
for permutation in permutations_of_ops:
    result = A[0]
    for i in range(1, N):
        result = compute(result, A[i], permutation[i-1])
    _max = max(_max, result)
    _min = min(_min, result)

print(_max)
print(_min)