import sys
input=sys.stdin.readline
N = int(input())
students = []
for _ in range(N):
    line = input().split()
    students.append((line[0], int(line[1]), int(line[2]), int(line[3])))
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in students:
    print(s[0])