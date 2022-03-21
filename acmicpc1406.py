# time limit exceeded

import sys
input = sys.stdin.readline
_str = list(input().rstrip())
p = len(_str)
M = int(input())
for _ in range(M):
    c = input().split()
    if c[0] == 'L' and p > 0:
        p -= 1
    elif c[0] == 'D' and p < len(_str):
        p += 1
    elif c[0] == 'B' and p > 0:
        del _str[p-1]
        p -= 1
    elif c[0] == 'P':
        _str.insert(p, c[1])
        p += 1

print(''.join(_str))