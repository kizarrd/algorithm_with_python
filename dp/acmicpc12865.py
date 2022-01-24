N, K = map(int, input().split())
stuff = [None]
V = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N+1):
    for w in range(1, K+1):
        if stuff[i][0] <= w and stuff[i][1] + V[i-1][w-stuff[i][0]] > V[i-1][w]:
            V[i][w] = stuff[i][1] + V[i-1][w-stuff[i][0]]
        else:
            V[i][w] = V[i-1][w]

print(V[N][K])