#1로 만들기
def makeOne(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 1
    memo = [0]*(n+1)
    memo[1] = 0
    memo[2] = 1
    memo[3] = 1
    for i in range(4, n+1):
        min = 1+memo[i-1]
        if i%2==0:
            divideByTwo = 1+memo[i//2]
            min = min if min<=divideByTwo else divideByTwo
        if i%3==0:
            divideByThree = 1+memo[i//3]
            min = min if min<=divideByThree else divideByThree
        memo[i] = min
    return memo[n]

n = int(input())
print(makeOne(n))