N, K = map(int, input().split())
denominations = []
for _ in range(N):
    denominations.append(int(input()))

cnt = 0
for i in range(N-1, -1, -1):
    if denominations[i] <= K:
        cnt += K//denominations[i]
        K = K%denominations[i]

print(cnt)