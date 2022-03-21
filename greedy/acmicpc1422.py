K, N = map(int, input().split())
numbers = [input() for _ in range(K)]
_max = max(numbers, key=lambda x: int(x))
for _ in range(N-K):
    numbers.append(_max)
for i in range(1, N):
    before_swap = ''.join(numbers)
    for j in range(i, 0, -1):
        numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
        after_swap = ''.join(numbers)
        if after_swap < before_swap:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            break
        else:
            before_swap = after_swap

print(''.join(numbers))