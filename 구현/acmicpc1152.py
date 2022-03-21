from collections import Counter
_str = input().upper()
if len(_str) == 1:
    print(_str)
    exit()
c = Counter(_str)
a, b = c.most_common(2)
print(a[0] if a[1] != b[1] else '?')