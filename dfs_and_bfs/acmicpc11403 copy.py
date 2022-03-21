import sys
input=sys.stdin.readline

N = int(input())
adj_m = [list(map(int, input().split())) for _ in range(N)]

for m in range(N):
    for i in range(N):
        for j in range(N):
            if not adj_m[i][j] and adj_m[i][m] and adj_m[m][j]:
                adj_m[i][j] = 1

for r in adj_m:
    print(*r)