import sys
input=sys.stdin.readline
A, B, C = map(int, input().split())

d = set()

def dfs(a, b, c):
    if (a, b, c) in d:
        return
    else:
        d.add((a, b, c))
    if a > 0:
        if b < B:
            if B-b >= a: dfs(0, b+a, c)
            else: dfs(a-(B-b), B, c)
        if c < C:
            if C-c >= a: dfs(0, b, c+a)
            else: dfs(a-(C-c), b, C)
    if b > 0:
        if a < A:
            if A-a >= b: dfs(a+b, 0, c)
            else: dfs(A, b-(A-a), c)
        if c < C:
            if C-c >= b: dfs(a, 0, c+b)
            else: dfs(a, b-(C-c), C)
    if c > 0:
        if a < A:
            if A-a >= c: dfs(a+c, b, 0)
            else: dfs(A, b, c-(A-a))
        if b < B:
            if B-b >= c: dfs(a, b+c, 0)
            else: dfs(a, B, c-(B-b))

dfs(0, 0, C)
answer = set()
for a, b, c in d:
    if a == 0:
        answer.add(c)

answer = sorted(list(answer))

for c in answer:
    print(c, end=' ')