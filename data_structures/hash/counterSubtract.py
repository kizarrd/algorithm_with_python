import collections

list1 = ['eden', 'eden','eden', 'son', 'leo','leo', 'kangin']
list2 = ['eden', 'son', 'leo', 'kangin']

answer = collections.Counter(list1)-collections.Counter(list2)
print(answer)
print(list(answer.keys()))
print(list(answer.values()))

#output: 
# Counter({'eden': 2, 'leo': 1})
# ['eden', 'leo']
# [2, 1]