import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def union(a, b):
    fa, fb = find(a), find(b)
    fal, fbl = friends[fa][1], friends[fb][1]
    if fa == fb:
        return
    else:
        if fa < fb:
            friends[fb] = [fa, fal+fbl]
            friends[fa][1] = fal+fbl
        else:
            friends[fa] = [fb, fal+fbl]
            friends[fb][1] = fal+fbl

def find(n):
    if friends[n][0] == n:
        return n
    root = find(friends[n][0])
    friends[n][0] = root
    return root

t = int(input())
for _ in range(t):
    F = int(input())
    friends = {}
    for _ in range(F):
        a, b = input().split()
        if a not in friends:
            friends[a] = [a, 1]
        if b not in friends:
            friends[b] = [b, 1]
        union(a, b)
        print(friends[find(a)][1])