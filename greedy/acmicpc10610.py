import sys
input=sys.stdin.readline

N = input().strip()
if '0' not in N:
    print(-1)
else:
    if sum(list(map(int, N)))%3 == 0:
        print(''.join(sorted(N, reverse=True)))
    else:
        print(-1)