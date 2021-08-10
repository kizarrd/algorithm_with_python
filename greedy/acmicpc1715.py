#카드 정렬하기
from queue import PriorityQueue

n = int(input())
q = PriorityQueue()
result = 0

for i in range(n):
    q.put(int(input()))

while q.qsize() >= 2:
    a = q.get()
    b = q.get()
    result += a+b
    q.put(a+b)

print(result)