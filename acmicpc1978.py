import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))

cnt = 0

for n in numbers:
    if n == 1:
        continue
    prime = True
    for i in range(2, int(n**(0.5)+1)):
        if n%i == 0:
            prime = False
            break
    if prime:
        cnt += 1

print(cnt)