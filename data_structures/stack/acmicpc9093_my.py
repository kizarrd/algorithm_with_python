#단어 뒤집기 문제
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    sentence = input().split()
    for word in sentence:
        wordStack = []
        for i in range(len(word)):
            wordStack.append(word[i])
        for j in range(len(word)):
            print(wordStack.pop(), end="")
        print("", end=" ")
    print("")