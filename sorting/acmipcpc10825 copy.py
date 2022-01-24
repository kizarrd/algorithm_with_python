import sys
input=sys.stdin.readline
N = int(input())
students = [input() for _ in range(N)]
students.sort(key=lambda x: (-int(x.split()[1]), int(x.split()[2]), -int(x.split()[3]), x.split()[0]))
for s in students:
    print(s.split()[0])