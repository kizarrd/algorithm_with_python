import sys
input=sys.stdin.readline
N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 0
prev = 0
for start, end in meetings:
    if start >= prev:
        cnt += 1
        prev = end

print(cnt)