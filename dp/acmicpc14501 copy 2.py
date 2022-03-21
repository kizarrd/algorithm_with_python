N = int(input())
T, P = [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

d = [0]*(N+2) 
for i in range(N, 0, -1):
    if T[i] > N-i+1:
        d[i] = d[i+1]
    else:
        d[i] = max(P[i]+d[i+T[i]], d[i+1])

print(d[1])