import sys
input=sys.stdin.readline
N = int(input())
steps = [0] + [int(input()) for _ in range(N)]
# d[n] = max point when including step n
d = [0]*301
d[1] = steps[1]
if N > 1:
    d[2] = steps[1]+steps[2]

for i in range(3, N+1):
    d[i] = max(d[i-2]+steps[i], d[i-3]+steps[i-1]+steps[i])

print(d[N])