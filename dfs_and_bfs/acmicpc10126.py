import sys
input=sys.stdin.readline

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    parents[fa] = fb

def find(n):
    if n == parents[n]:
        return n
    parents[n] = find(parents[n])
    return parents[n]

T = int(input())
for _ in range(T):
    N = int(input())
    parents = list(range(N+1))
    comms = []
    for i in range(1, N+1):
        x, y, R = map(int, input().split())
        for x1, y1, r1, i1 in comms:
            if (x1-x)**2+(y1-y)**2 <= (r1+R)**2:
                union(i1, i)
        comms.append((x, y, R, i))

    distinct_area = set()
    for i in range(1, N+1):
        distinct_area.add(find(i))
    print(len(distinct_area))