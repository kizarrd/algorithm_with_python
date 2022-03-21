from bisect import bisect_left
import sys
input=sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
integers = list(map(int, input().split()))

for target in integers:
    i = bisect_left(cards, target)
    print(1 if i < N and cards[i] == target else 0, end=' ')