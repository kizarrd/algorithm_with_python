import sys
input=sys.stdin.readline

G = int(input())
P = int(input())

def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    parents[fa] = fb

parents = list(range(G+1))

planes = [0]+[int(input()) for _ in range(P)]

for i in range(1, P+1):
    g = find(planes[i])
    fg = find(g)
    if fg > 0:
        union(fg, fg-1)
    else:
        print(i-1)
        exit()

print(P)