import sys
input=sys.stdin.readline
N = int(input())
meetings = []

for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_last_m = 0
for start, end in meetings:
    if start >= end_last_m:
        cnt += 1
        end_last_m = end

print(cnt)