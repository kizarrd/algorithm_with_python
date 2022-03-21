# union-find, with very very inefficient DFS

import sys
input=sys.stdin.readline
N = int(input())
coordinates = [[0]*1001 for _ in range(1001)]
# draw rectangles
shift = 500
starting_points = []

def merge(x, y, i, j):
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    stack = []
    stack.append((x, y))
    coordinates[x][y] = i
    while stack:
        sx, sy = stack.pop()
        for dx, dy in moves:
            nx, ny = sx+dx, sy+dy
            if 0<=nx<=1000 and 0<=ny<=1000 and coordinates[nx][ny] == j:
                coordinates[nx][ny] = i
                stack.append((nx, ny))

for i in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1+shift, y1+shift, x2+shift, y2+shift
    starting_points.append((x1, y1))
    for x in range(x1, x2+1):
        if coordinates[x][y1] and coordinates[x][y1] != i:
            merge(x, y1, i, coordinates[x][y1])
        if coordinates[x][y2] and coordinates[x][y2] != i:
            merge(x, y2, i, coordinates[x][y2])
        coordinates[x][y1] = i
        coordinates[x][y2] = i
    for y in range(y1+1, y2):
        if coordinates[x1][y] and coordinates[x1][y] != i:
            merge(x1, y, i, coordinates[x1][y])
        if coordinates[x2][y] and coordinates[x2][y] != i:
            merge(x2, y, i, coordinates[x2][y])
        coordinates[x1][y] = i
        coordinates[x2][y] = i

separate_groups = set()
for x, y in starting_points:
    separate_groups.add(coordinates[x][y])

if coordinates[shift][shift]:
    print(len(separate_groups)-1)
else:
    print(len(separate_groups))