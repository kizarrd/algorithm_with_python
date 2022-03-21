N = int(input())

primes = [True]*(N+1)
primes[0], primes[1] = False, False

for i in range(2, int(len(primes)**0.5)+1):
    if primes[i]:
        for j in range(2*i, len(primes), i):
            primes[j] = False

number = N
for d in range(1, N+1):
    if number == 1:
        break
    if primes[d]:
        while number%d == 0:
            print(d)
            number//=d