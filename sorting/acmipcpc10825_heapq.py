from heapq import heappush, heappop
import sys
input=sys.stdin.readline
N = int(input())
students = []
for _ in range(N):
    line = input().split()
    heappush(students, (-int(line[1]), int(line[2]), -int(line[3]), line[0]))

while students:
    print(heappop(students)[3])