N = int(input())
primes = [True]*(N+1)
primes[0], primes[1] = False, False
for i in range(2, int(len(primes)**0.5)+1):
    if primes[i]:
        for j in range(i*i, len(primes), i):
            primes[j] = False
only_primes = [i for i, v in enumerate(primes) if v]
cnt = 0
left, right = 0, 0
_sum = 0
while True:
    if _sum >= N:
        if _sum == N:
            cnt += 1
        _sum -= only_primes[left]
        left += 1
    elif right == len(only_primes):
        break
    elif _sum < N:
        _sum += only_primes[right]
        right += 1

print(cnt)