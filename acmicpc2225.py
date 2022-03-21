from math import factorial
N, K = map(int, input().split())
h = factorial(N+K-1)//(factorial(N)*factorial(K-1))
print(h%1000000000)