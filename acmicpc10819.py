from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

def getValue(arr):
    _sum = 0
    for i in range(len(arr)-1):
        _sum += abs(arr[i]-arr[i+1])
    return _sum

perms = permutations(A, len(A))

print(max(map(lambda p: getValue(p), perms)))