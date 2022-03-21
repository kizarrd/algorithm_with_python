N = int(input())
T, P = [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
# d[i] = max_profit when working until day i --> O(1+...+N)?
d = [0]*(N+1)
for i in range(1, N+1):
    P_if_can_do_Ti = P[i] if N-i+1 >= T[i] else 0
    d[i] = P_if_can_do_Ti
    for j in range(i-1, 0, -1):
        if i-j+1 == T[j]:
            d[i] = max(d[i], d[j])
        elif i-j+1 > T[j]:
            d[i] = max(d[i], d[j]+P_if_can_do_Ti)

print(d[N])