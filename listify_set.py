s1 = { 3, 2, 1 }
a_list = list(s1)
b_list = [s1]
a_list.sort()
b_list.sort()
print(a_list)
print(b_list)
print(b_list[0])
print(type(b_list[0]))
print(sorted(s1))