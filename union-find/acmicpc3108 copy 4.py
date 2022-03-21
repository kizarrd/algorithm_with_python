import sys
input=sys.stdin.readline
N = int(input())
parents = [0]+list(range(1, N+1))
rank = [0]*(N+1)
visited = [[0]*1001 for _ in range(1001)]

def find(n):
    if parents[n] == n:
        return n
    parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        parents[ra] = rb
    else:
        parents[rb] = ra
        rank[ra] += 1

for n in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2+1):
        if visited[x][y1]:
            union(visited[x][y1], n)
        visited[x][y1] = n
        if visited[x][y2]:
            union(visited[x][y2], n)
        visited[x][y2] = n
        
    for y in range(y1, y2+1):
        if visited[x1][y]:
            union(visited[x1][y], n)
        visited[x1][y] = n
        if visited[x2][y]:
            union(visited[x2][y], n)
        visited[x2][y] = n
    
cnt = len(set(find(i) for i in range(1, N+1))) - 1
if not visited[0][0]:
    cnt += 1

print(cnt)