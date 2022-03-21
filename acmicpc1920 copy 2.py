import sys
input=sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

for target in numbers:
    print(1 if target in A else 0)