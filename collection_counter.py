import collections

a = ['a', 'c', 'b', 'c', 'c', 'b']
b = 'hello world'
c = {'first': 'a', 'second': 'b'}
d = ('a', 'b', 'c', 'd')

a_counter = collections.Counter(a)
b_counter = collections.Counter(b)
c_counter = collections.Counter(c)
d_counter = collections.Counter(d)

print(a_counter)
print(type(a_counter))
print(b_counter)
print(type(c))
print(c_counter)
print(type(d))
print(d_counter)
