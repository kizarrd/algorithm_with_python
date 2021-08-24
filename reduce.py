from functools import reduce 

t = [47, 11, 42, 13]

result = reduce(lambda x, y : x + y, t)
print(result)

result = reduce(lambda x, y : x - y, t)
print(result)

result = reduce(lambda x, y : x * y, t)
print(result)

# output:
# 113
# -19
# 282282