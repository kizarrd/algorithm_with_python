N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0
B.sort(reverse=True)
A.sort()
for a, b in zip(A, B):
    S += a*b

print(S)