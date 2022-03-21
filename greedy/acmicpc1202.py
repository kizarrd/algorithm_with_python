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
    for i in range(K):
        if not bag_full[i] and M <= C[i]:
            bag_full[i] = 1
            price += V
            break
    if all(bag_full):
        print(price)
        exit()
print(price)