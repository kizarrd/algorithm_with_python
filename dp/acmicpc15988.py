d = [0]*1000001
mod = 1000000009
d[0] = 1; d[1] = 2; d[2] = 4

for i in range(1, 1000000+1):
    d[i] = d[i-1]+d[i-2]+d[i-3]
    d[i] %= mod

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])