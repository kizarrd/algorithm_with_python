import sys
input = sys.stdin.readline

n = int(input())
s = n

for i in range(1, n+1):
    s-=i
    if s<=i :
        print(i)
        break