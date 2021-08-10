#분해합
# bhh = 분해합
N = int(input())

def getBhh(i):
    numStr = str(i)
    sum = 0
    for numInEachDigit in numStr:
        sum += int(numInEachDigit)
    return sum

for i in range(1, N+1):
    difference = N-i
    bhh = getBhh(i)
    if bhh == difference:
        print(i)
        exit()
        
print(0)