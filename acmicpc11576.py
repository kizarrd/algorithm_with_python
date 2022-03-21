A, B = map(int, input().split())
n = int(input())
number_A = list(map(int, input().split()))
# convert A to 10
n_ten = 0
m = 1
for d in number_A[::-1]:
    n_ten += d*m
    m *= A
# convert the converted to B
n_B = []
m = 1
while n_ten > m:
    m *= B

m //= B
while True:
    n_B.append(n_ten//m)
    if m == 1:
        break
    n_ten %= m
    m //= B

print(*n_B)