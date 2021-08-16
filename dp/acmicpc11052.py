#카드 구매하기
n = int(input())
inputList = list(map(int, input().split()))
p = [0]*(n+1)
for i in range(1, n+1):
    p[i] = inputList[i-1]

for j in range(1, n+1):
    max = p[j]
    for k in range(1, (j//2)+1):
        if max < p[j-k]+p[k]:
            max = p[j-k]+p[k]
    p[j] = max

print(p[n])