import sys
input = sys.stdin.readline
n = int(input())

wines = [int(input()) for _ in range(n)]
if n==1:
    print(wines[0])
    exit()

d = [0]*(n+1)
d[1] = wines[0]
d[2] = wines[0]+wines[1]

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-2]+wines[i-1], d[i-3]+wines[i-1]+wines[i-2])

print(d[n])