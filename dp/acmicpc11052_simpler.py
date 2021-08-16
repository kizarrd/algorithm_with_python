#카드 구매하기
n = int(input())
p = [0]+list(map(int, input().split()))

for i in range(1, n+1):
    maxSofar = p[i]
    for j in range(1, (i//2)+1):
        maxSofar = max(maxSofar, p[i-j]+p[j])
    p[i] = maxSofar

print(p[n])