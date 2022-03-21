from collections import defaultdict
import sys
input=sys.stdin.readline

A, B, C, D = [], [], [], []

n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

a_plus_b = defaultdict(int)
for a in A:
    for b in B:
        a_plus_b[a+b] += 1

cnt = 0
for c in C:
    for d in D:
        if -(c+d) in a_plus_b:
            cnt += a_plus_b[-(c+d)]

print(cnt)