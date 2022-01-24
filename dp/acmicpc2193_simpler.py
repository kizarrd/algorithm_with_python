N = int(input())
if N == 1:
    print(1)
    exit()

d = [0]*(N+1)
d[1], d[2] = 1, 1
for i in range(3, N+1):
    d[i] = d[i-1]+d[i-2]

print(d[N])