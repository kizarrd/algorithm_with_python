from collections import deque
import sys
input=sys.stdin.readline

cog = [0]
for _ in range(4):
    cog.append(deque(map(int, input().rstrip())))
K = int(input())

left, right = 6, 2
def rotate_cog(n, dir):
    if n >= 2 and not visited[n-1] and cog[n][left] != cog[n-1][right]:
        visited[n-1] = 1
        rotate_cog(n-1, -dir)
    if n <= 3 and not visited[n+1] and cog[n][right] != cog[n+1][left]:
        visited[n+1] = 1
        rotate_cog(n+1, -dir)
    cog[n].rotate(dir)

for _ in range(K):
    visited = [0]*5
    n, dir = map(int, input().split())
    visited[n] = 1
    rotate_cog(n, dir)

up = 0
total_score = 0
score = 1
for n in range(1, 5):
    total_score += cog[n][up]*score
    score *= 2

print(total_score)