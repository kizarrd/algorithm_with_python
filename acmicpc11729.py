N = int(input())
def hanoi(n, i, j, k):
    if n == 1:
        answers.append((i, k))
        return
    hanoi(n-1, i, k, j)
    hanoi(1, i, j, k)
    hanoi(n-1, j, i, k)

answers = []
hanoi(N, 1, 2, 3)
print(len(answers))
for a, b in answers:
    print(a, b)