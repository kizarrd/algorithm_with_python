N = int(input())

one_zero = 2
zeros = 1
for _ in range(2, N+1):
    one_zero, zeros = (one_zero+zeros*2), zeros+one_zero

print((one_zero+zeros)%9901)