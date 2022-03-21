import sys
input=sys.stdin.readline
N = int(input())
coords = []
for _ in range(N):
    coords.append(list(map(int, input().split())))

coords.sort(key=lambda x: (x[1], x[0]))
for x, y in coords:
    print(x, y)