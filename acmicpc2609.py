N, M = map(int, input().split())
a, b = N, M
r = None
while b != 0:
    r = a%b
    a, b = b, r
print(a)
print(N*M//a)