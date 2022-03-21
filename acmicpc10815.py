import sys
input=sys.stdin.readline

N = int(input())
cards = set(list(map(int, input().split())))
M = int(input())
integers = list(map(int, input().split()))

for i in integers:
    print(1 if i in cards else 0, end=' ')