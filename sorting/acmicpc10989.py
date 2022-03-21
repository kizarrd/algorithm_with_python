import sys
input=sys.stdin.readline
N = int(input())

counter = [0]*10001
for _ in range(N):
    counter[int(input())] += 1

for i in range(len(counter)):
    for _ in range(counter[i]):
        print(i)