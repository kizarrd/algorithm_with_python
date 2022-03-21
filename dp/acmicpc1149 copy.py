import sys
input=sys.stdin.readline

N = int(input())
cost = [0]+[list(map(int, input().split())) for _ in range(N)]
d = cost[1][:]

for i in range(2, N+1):
    r, g, b = cost[i]
    r_prev, g_prev, b_prev = d
    d[0] = min(r+g_prev, r+b_prev)
    d[1] = min(g+r_prev, g+b_prev)
    d[2] = min(b+r_prev, b+g_prev)

print(min(d))