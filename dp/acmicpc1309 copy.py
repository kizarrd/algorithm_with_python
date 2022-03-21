N = int(input())

prev = [1, 1, 1]
for i in range(2, N+1):
    left, right, empty = prev
    prev[0] = (right + empty)%9901
    prev[1] = (left + empty)%9901
    prev[2] = (left + right + empty)%9901

print(sum(prev)%9901)