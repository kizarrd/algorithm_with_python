import sys
input=sys.stdin.readline

N, M, K = map(int, input().split())

numbers = [0]*(N+1)
tree = [0]*(N+1)

def update(index, n):
    i = index
    diff = n - numbers[i]
    while i <= N:
        tree[i] += diff
        i += (i & -i)

def prefix_sum(end):
    _sum = 0
    i = end
    while i > 0:
        _sum += tree[i]
        i -= (i & -i)
    
    return _sum

def interval_sum(left, right):
    return prefix_sum(right) - prefix_sum(left-1)

for i in range(1, N+1):
    a = int(input())
    update(i, a)
    numbers[i] = a

answers = []

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
        numbers[b] = c
    else:
        answers.append(interval_sum(b, c))

print(*answers, sep='\n')