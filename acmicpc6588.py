import sys
input=sys.stdin.readline
# sieve
primes = [True]*(10**6+1)
primes[0], primes[1] = False, False
for i in range(2, 10**3+1):
    if primes[i]:
        m = i
        while i*m <= 10**6:
            primes[i*m] = False
            m += 1

while True:
    n = int(input())
    if n == 0: break
    found = False
    for i in range(3, (10**6)//2 + 1):
        if primes[i] and primes[n-i]:
            print(f'{n} = {i} + {n-i}')
            found = True
            break
    if not found:
        print("Goldbach's conjecture is wrong.")