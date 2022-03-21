import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def union(a, b):
    ra, rb = find(a), find(b) # root a and root b
    if ra == rb:
        print(size[ra])
        return
    friends[ra] = rb
    size[rb] = size[rb]+size[ra]
    print(size[rb])

def find(n):
    if friends[n] == n:
        return n
    friends[n] = find(friends[n])
    return friends[n]

t = int(input())
for _ in range(t):
    F = int(input())
    friends = {}
    size = {}
    for _ in range(F):
        a, b = input().split()
        if a not in friends:
            friends[a] = a
            size[a] = 1
        if b not in friends:
            friends[b] = b
            size[b] = 1
        union(a, b)