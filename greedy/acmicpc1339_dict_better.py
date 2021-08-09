N = int(input())
words = []
priorities = {}
for _ in range(N):
    words.append(input())

for word in words:
    power = len(word)-1
    for character in word:
        if character not in priorities:
            priorities[character] = 0
        priorities[character] += 10**power
        power -= 1

valuesSorted = sorted(list(priorities.values()), reverse = True)

sum = 0
multiplier = 9
for valueOfCharacter in valuesSorted:
    sum += valueOfCharacter*multiplier
    multiplier -= 1

print(sum)