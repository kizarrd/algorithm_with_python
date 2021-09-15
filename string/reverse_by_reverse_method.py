# array.reverse()를 string에 써보기

a_string = "string!"

# a_string.reverse()
# 이거 안되네 에러나네?

# a_string.sort()
#얘도 해봤는데 에러나네. 잘못알고있었군.

a_list = list(a_string)
print(a_list)

a_list.reverse()
print(str(a_list))
print(''.join(a_list))