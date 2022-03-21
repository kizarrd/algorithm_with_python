N, B = map(int, input().split())

def getAlpha(n):
    return chr(ord('A')+n-10)

answer = []

while N//B > 0:
    n_digit = N%B if N%B < 10 else getAlpha(N%B)
    N //= B
    answer.append(n_digit)
n_digit = N%B if N%B < 10 else getAlpha(N%B)
answer.append(n_digit)

print(*answer[::-1], sep='')