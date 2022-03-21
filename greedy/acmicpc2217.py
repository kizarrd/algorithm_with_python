import sys
input=sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)

max_w = 0
for i in range(N):
    max_w = max(max_w, ropes[i]*(i+1))

print(max_w)