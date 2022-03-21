from collections import Counter
import sys
input=sys.stdin.readline
_ = input()
cards = Counter(map(int, input().split()))
M = int(input())
integers = list(map(int, input().split()))
for i in range(M):
    if i > 0:
        print(' ', end='')
    print(cards[integers[i]], end='')