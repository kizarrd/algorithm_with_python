import sys
input=sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
integers = list(map(int, input().split()))

def binary_search(target, start, end):
    if start > end:
        return 0

    mid = (start+end)//2
    if target == cards[mid]:
        return 1
    elif target < cards[mid]:
        return binary_search(target, start, mid-1)
    else: # if target > cards[mid]
        return binary_search(target, mid+1, end)

for target in integers:
    print(binary_search(target, 0, N-1), end=' ')