N = int(input())
d = [0]*(N+1)
for n in range(1, int(N**0.5)+1):
    d[n**2] = 1

squares = [j*j for j in range(1, int(N**0.5)+1)]

for i in range(2, N+1):
    s = []
    for sq in squares:
        if sq > i: break 
        s.append(d[sq] + d[i-sq])
    d[i] = min(s)

print(d[N])