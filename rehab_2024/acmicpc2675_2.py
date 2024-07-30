import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  R, S = input().split()
  R = int(R)
  result = ''
  for char in S:
    char_series = char*R
    result += char_series
  print(result)