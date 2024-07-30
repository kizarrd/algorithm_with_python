import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  R, S = input().split()
  R = int(R)
  for char in S:
    print(''.join([char for _ in range(R)]), end='')
  print()