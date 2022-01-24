import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(input().split()) for _ in range(N)]
arr.sort(key=lambda x: (int(x[0])))
for age, name in arr:
    print(age, name) 