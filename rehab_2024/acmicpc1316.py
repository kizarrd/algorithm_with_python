import sys
input=sys.stdin.readline

N=int(input())

cnt = 0
for _ in range(N):
  word = input()
  last_char = word[0]
  discovered = [last_char]
  group_word = True
  for char in word:
    if char != last_char:
      if char in discovered:
        group_word = False
        break
      else:
        discovered.append(char)
    last_char = char
  if group_word:
    cnt += 1

print(cnt)