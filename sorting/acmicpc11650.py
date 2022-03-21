import sys
input=sys.stdin.readline
N = int(input())
_list = [list(map(int, input().split())) for _ in range(N)]
for x, y in sorted(_list, key=lambda x: (x[0], x[1])):
    print(x, y)