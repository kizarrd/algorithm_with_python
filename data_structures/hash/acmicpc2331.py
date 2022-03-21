A, P = map(int, input().split())

def getNextNum(num):
    _sum = 0
    while num//10 > 0:
        _sum += (num%10)**P
        num //= 10
    _sum += (num)**P

    return _sum

check_repetition = {}

num_curr = A
i = 0
nums = []
while num_curr not in check_repetition:
    check_repetition[num_curr] = i
    nums.append(num_curr)
    i += 1
    num_curr = getNextNum(num_curr)

print(check_repetition[num_curr])