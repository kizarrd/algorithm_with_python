import sys
input=sys.stdin.readline
N = int(input())
paper = [[0]*100 for _ in range(100)]
for _ in range(N):
    ls, bs = map(int, input().split()) # left start, bottom start
    for r in range(bs, bs+10):
        for c in range(ls, ls+10):
            paper[r][c] = 1

print(sum(sum(row) for row in paper))