# union-find, wild

import sys
input=sys.stdin.readline
N = int(input())
coordinates = [[0]*1001 for _ in range(1001)]
# draw rectangles
shift = 500
starting_points = []

identities = [n-1 for n in range(1, N+2)]
def merge(i, j):
    for n in range(len(identities)):
        if identities[n] == j:
            identities[n] = i

for i in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1+shift, y1+shift, x2+shift, y2+shift
    starting_points.append((x1, y1))
    for x in range(x1, x2+1):
        if coordinates[x][y1] and identities[coordinates[x][y1]] != i:
            merge(i, identities[coordinates[x][y1]])
        if coordinates[x][y2] and identities[coordinates[x][y2]] != i:
            merge(i, identities[coordinates[x][y2]])
        coordinates[x][y1] = i
        coordinates[x][y2] = i
    for y in range(y1+1, y2):
        if coordinates[x1][y] and identities[coordinates[x1][y]] != i:
            merge(i, identities[coordinates[x1][y]])
        if coordinates[x2][y] and identities[coordinates[x2][y]] != i:
            merge(i, identities[coordinates[x2][y]])
        coordinates[x1][y] = i
        coordinates[x2][y] = i

separate_groups = set()
for i in range(1, len(identities)):
    separate_groups.add(identities[i])

if coordinates[shift][shift]:
    print(len(separate_groups)-1)
else:
    print(len(separate_groups))