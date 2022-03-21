import sys
input=sys.stdin.readline
n, m = map(int, input().split())

# make sets
parents = [i for i in range(n+1)]

def checkSame(a, b):
    if find(a) == find(b):
        return 'YES'
    else:
        return 'NO'

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    else:
        if fa < fb:
            parents[fa] = fb
        else:
            parents[fb] = fa

def find(n):
    if parents[n] == n:
        return n
    else:
        root = find(parents[n])
        parents[n] = root
        return root


for _ in range(m):
    c, a, b = map(int, input().split())
    if c:
        print(checkSame(a, b))
    else:
        union(a, b)