N = int(input())
A = list(map(int, input().split()))
A.sort()

A_rev = A[::-1]
new_A = []
for i in range(len(A)//2):
    new_A.append(A_rev[i])
    new_A.append(A[i])

if len(A)%2 == 1:
    new_A.append(A[len(A)//2])

_sum = 0
for i in range(len(new_A)-1):
    _sum += abs(new_A[i]-new_A[i-1])

print(_sum)