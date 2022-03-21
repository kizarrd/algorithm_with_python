import sys
input=sys.stdin.readline
t = int(input())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

for _ in range(t):
    arr = list(map(int, input().split()))
    _sum = 0
    for i in range(1, ub:=arr[0]+1):
        for j in range(i+1, ub):
            _sum += gcd(arr[i], arr[j])
    print(_sum)