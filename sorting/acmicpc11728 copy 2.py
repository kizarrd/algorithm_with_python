import sys
input=sys.stdin.readline
N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)

while A or B:
    if A and not B:
        print(A.pop(), end=' ')
    elif B and not A:
        print(B.pop(), end=' ')
    else:
        if A[-1] < B[-1]:
            print(A.pop(), end=' ')
        else:
            print(B.pop(), end=' ')
