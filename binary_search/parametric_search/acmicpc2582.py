# parametric search + bfs
from collections import deque
import math
import sys
input=sys.stdin.readline

size = 10000

n, k = map(int, input().split())
airports = [[0, 0]]+[list(map(int, input().split())) for _ in range(n)]+[[size, size]]

def get_dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def bfs(reachable_distance):
    q = deque()
    q.append((0, 0, 0)) # x, y, number of airports visited
    while q:
        x1, y1, d = q.popleft()
        if d == k+1:
            return False
        for i in range(1, n+2):
            if not visited[i]:
                x2, y2 = airports[i]
                if get_dist(x1, y1, x2, y2) <= reachable_distance:
                    visited[i] = 1
                    if x2 == size == y2:
                        return True
                    q.append((x2, y2, d+1))
    return False

lo, hi = 1, math.ceil(get_dist(0, 0, size, size)/10)
answer = 0
while lo <= hi:
    mid = (lo+hi)//2
    visited = [0]*(n+2)
    visited[0] = 1
    if bfs(mid*10):
        answer = mid
        hi = mid-1
    else:
        lo = mid+1

print(answer)