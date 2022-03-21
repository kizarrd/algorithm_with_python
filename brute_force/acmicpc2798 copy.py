from itertools import combinations
import sys
input=sys.stdin.readline
_, M = map(int, input().split())
cards = list(map(int, input().split()))

print(max(i for i in map(sum, combinations(cards, 3)) if i <= M))