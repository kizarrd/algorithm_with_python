N = int(input())

d = [[0, 0, 0] for _ in range(N+1)]
d[1] = [1, 1, 1]
for i in range(2, N+1):
    d[i][0] = (d[i-1][1] + d[i-1][2])%9901
    d[i][1] = (d[i-1][0] + d[i-1][2])%9901
    d[i][2] = (sum(d[i-1]))%9901

print(sum(d[N])%9901)