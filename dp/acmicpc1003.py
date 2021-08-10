#피보나치 함수
fibonacci = [0, 1]

for i in range(2, 41):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

def countZero(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci[n-1]

def countOne(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci[n]

n = int(input())
for _ in range(n):
    x = int(input())
    print(countZero(x), countOne(x))