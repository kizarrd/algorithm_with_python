import sys
input=sys.stdin.readline
N, K = map(int, input().split())
countries = []
for _ in range(N):
    k, G, S, B = map(int, input().split())
    if k == K:
        gK, sK, bK = G, S, B
    else:
        countries.append((k, G, S, B))

cnt = 0
for k, G, S, B in countries:
    if G > gK:
        cnt += 1
    elif G == gK:
        if S > sK:
            cnt += 1
        elif S == sK:
            if B > bK:
                cnt += 1

print(cnt+1)