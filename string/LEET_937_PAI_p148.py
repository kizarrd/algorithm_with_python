# 띄어쓰기 다를때 sort는 어떻게 되는걸까?

a = "abc def"
b = "ab cdef"
#이러면 cdef가 def보다 lexicographically small이므로 b가 먼저 오게 되려나?
#아니다. b가 먼저 오는건 맞는데 그 이유는 
# ab가 abc보다 lexicographically small이므로 b가 먼저 오게 된다.

a_list = [a, b]

a_list.sort(key=lambda x: x.split())

print(a_list)