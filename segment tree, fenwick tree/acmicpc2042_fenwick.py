import sys
input=sys.stdin.readline

# Fenwick Tree
N, M, K = map(int, input().split())
nums = [0]*(N+1)
tree = [0]*(N+1)

def update(i, n):
    diff = n-nums[i]
    while i <= N:
        tree[i] += diff
        i += (i & -i)

def prefix_sum(i):
    _sum = 0
    while i > 0:
        _sum += tree[i]
        i -= (i & -i)
    return _sum

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1, N+1):
    n = int(input())
    update(i, n)
    nums[i] = n

answers = []
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
        nums[b] = c
    else:
        answers.append(interval_sum(b, c))

print(*answers, sep='\n')