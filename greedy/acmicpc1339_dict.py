#단어 수학
import sys
input = sys.stdin.readline

N = int(input())
words = []
valueList = {}
for i in range(N):
    words.append(input())

for word in words:
    for i in range(1, len(word)):
        character = word[::-1][i]
        if character not in valueList:
            valueList[character] = 0
        valueList[character] += 10**(i-1)

valueList_sorted = dict(sorted(valueList.items(), key=lambda item: item[1], reverse=True))

multiplier = 9
sum = 0
for k, v in valueList_sorted.items():
    sum += v*multiplier
    multiplier -= 1

print(sum)