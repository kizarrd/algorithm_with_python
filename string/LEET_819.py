from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# for char in paragraph:
#     if not char.isalpha():
#         paragraph.replace(char, ' ')

for symbol in "!?',;.":
    print(symbol)
    paragraph = paragraph.replace(symbol, ' ')
    print(paragraph)

print(paragraph)

c = Counter(paragraph.lower().split()).most_common()

print(c)

# for word in c:
#     if word[0] in banned:
#         continue
#     else:
#         return word[0]