import sys
input=sys.stdin.readline
N = int(input())
seq = list(map(int, input().split()))

d = [1]*N
prev = [-1]*N
for i in range(N):
    for j in range(i):
        if seq[j] < seq[i] and d[j]+1 > d[i]:
            d[i] = d[j]+1
            prev[i] = j

max_idx = 0
max_d = max(d)
for i, v in enumerate(d):
    if v == max_d:
        max_idx = i
        break

answer = []
idx = max_idx
while idx > -1:
    answer.append(seq[idx])
    idx = prev[idx]

print(max_d)
while answer:
    print(answer.pop(), end=' ')