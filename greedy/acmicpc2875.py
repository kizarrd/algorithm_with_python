N, M, K = map(int, input().split())

while K:
    if M*2 >= N:
        M -= 1
    else:
        N -= 1
    K -= 1

_min = min(N, M*2)
print(_min//2)