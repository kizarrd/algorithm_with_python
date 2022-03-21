from itertools import product
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
products = product(numbers, repeat=M)
for seq in products:
    print(*seq)