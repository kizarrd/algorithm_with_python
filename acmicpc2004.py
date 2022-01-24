'''
nCm = n!/m!(n-m)!
'''
n, m = map(int, input().split())

def count_n(a, b):
    cnt = 0
    while a != 0:
        a //= b
        cnt += a
    return cnt
    
twos = count_n(n, 2) - count_n(m, 2) - count_n(n-m, 2)
fives = count_n(n, 5) - count_n(m, 5) - count_n(n-m, 5)

print(min(twos, fives))