N = int(input())

for _ in range(N):
    string = list(input().split())
    for i in string:
        print(i[::-1], end=' ')