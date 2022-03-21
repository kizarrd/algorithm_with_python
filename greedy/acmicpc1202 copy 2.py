from bisect import bisect_left
import sys
input=sys.stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
C = [int(input()) for _ in range(K)]
bag_full = [0]*K

jewels.sort(key=lambda x: (-x[1], x[0]))
C.sort()
price = 0
for M, V in jewels:
    if M <= C[-1]:
        i = bisect_left(C, M)
        price += V
        del C[i]
        if not C:
            break

print(price)