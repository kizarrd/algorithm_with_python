import sys
input=sys.stdin.readline

N = int(input())
num_list = input().strip()

num_sum = 0
for i in num_list:
  num_sum+=int(i)

print(num_sum)