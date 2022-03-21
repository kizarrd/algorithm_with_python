N = int(input())
d = [0]*(31)
d[0] = 1
d[1] = 0
d[2] = 3  # d[0]*3
d[3] = 0  # d[1]*3

for i in range(4, N+1):
    d[i] = d[i-2]*3
    if i%2 == 0:
        for j in range(4, i+1, 2):
            d[i] += d[i-j]*2
print(d[N])