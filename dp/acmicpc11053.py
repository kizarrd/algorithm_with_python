import sys
input=sys.stdin.readline
N = int(input())
seq = list(map(int, input().split()))

d = [1]*N
for i in range(N):
    for j in range(i):
        if seq[j] < seq[i] and d[j]+1 > d[i]:
            d[i] = d[j]+1

print(max(d))