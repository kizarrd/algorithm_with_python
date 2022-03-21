N = int(input())
d = [0]*(N+1)
for i in range(2, N+1):
    _min = d[i-1]+1
    if i%3 == 0: _min = _min if _min < d[i//3]+1 else d[i//3]+1
    if i%2 == 0: _min = _min if _min < d[i//2]+1 else d[i//2]+1
    d[i] = _min

print(d[N])