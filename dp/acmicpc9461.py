import sys
input = sys.stdin.readline

T = int(input())
while T:
    N = int(input())
    if 1 <= N <= 6:
        d = [0, 1, 1, 1, 2, 2, 3]
        print(d[N])
    else:
        d = [0]*(N+1)
        d[1], d[2], d[3], d[4], d[5], d[6] = 1, 1, 1, 2, 2, 3
        for i in range(7, N+1):
            d[i] = d[i-1]+d[i-5]
        print(d[N])
    T -= 1