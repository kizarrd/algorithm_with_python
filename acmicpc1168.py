import sys
input=sys.stdin.readline
N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]
p = []
j = -1
while arr:
    j += K
    j %= len(arr)
    p.append(arr.pop(j))
    j -= 1

print('<', end='')
print(*p, end='', sep=', ')
print('>')