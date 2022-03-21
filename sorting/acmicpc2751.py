import sys
input=sys.stdin.readline
N = int(input())
_list = []
for _ in range(N):
    _list.append(int(input()))

print(*sorted(_list), sep='\n')