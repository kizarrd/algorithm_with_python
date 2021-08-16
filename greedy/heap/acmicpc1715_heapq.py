#카드 정렬하기
import heapq

N = int(input())

# cardList = list(int(input()) for _ in range(N))
# heapq.heapify(cardList)

cardList = []
for _ in range(N):
    heapq.heappush(cardList, int(input()))

result=0

while len(cardList) != 1:
    num1 = heapq.heappop(cardList)
    num2 = heapq.heappop(cardList)
    Sum = num1 + num2
    result += Sum
    heapq.heappush(cardList,Sum)

print(result)