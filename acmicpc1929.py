M, N = map(int, input().split())
primes = [True]*(N+1)
primes[0], primes[1] = False, False
for i in range(2, int(N**0.5)+1):
    if primes[i]:
        for j in range(2*i, N+1, i):
            primes[j] = False

for i in range(M, N+1):
    if primes[i]: print(i)