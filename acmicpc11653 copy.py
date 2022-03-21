N = int(input())
number = N
for d in range(2, N+1):
    if number == 1:
        break
    while number%d == 0:
        print(d)
        number/=d