from bisect import bisect_left, bisect_right
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
integers = list(map(int, input().split()))
cards.sort()
answers = []
for i in range(M):
    start = bisect_left(cards, integers[i])
    if start < M and cards[start] == integers[i]:
        end = bisect_right(cards, integers[i])
        answers.append(end-start)
    else:
        answers.append(0)

print(*answers)