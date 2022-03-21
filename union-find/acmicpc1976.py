import sys
input=sys.stdin.readline

N = int(input())
M = int(input())

def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    if fa > fb:
        parents[fa] = fb
    else:
        parents[fb] = fa

parents = list(range(N+1))
for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(1, N+1):
        if row[j-1]:
            union(i, j)

travel_plan = list(map(int, input().split()))
prev = find(travel_plan[0])
for city in travel_plan:
    fc = find(city)
    if prev != fc:
        print('NO')
        exit()
    prev = fc

print('YES')