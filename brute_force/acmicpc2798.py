#블랙잭
n, m = map(int, input().split())
cards = list(map(int, input().split()))

maxNum = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = cards[i]+cards[j]+cards[k]
            if sum <= m and sum > maxNum :
                maxNum = sum
print(maxNum)