K, N = map(int, input().split())
numbers = [input() for _ in range(K)]
_max = max(numbers, key=lambda x: int(x))
for _ in range(N-K):
    numbers.append(_max)

for i in range(1, N):
    j = i
    while j > 0 and numbers[j-1]+numbers[j] < numbers[j]+numbers[j-1]:
        numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
        j -= 1

print(''.join(numbers))