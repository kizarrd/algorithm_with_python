a = [(1, 2), (5, 2), (0, 1), (5, 1), (3, 0)]

print( sorted(a) )
print( sorted(a, key = lambda x : x[0]) )
print( sorted(a, key = lambda x : -x[0]) )
print( sorted(a, key = lambda x : (x[0], x[1])) )
print( sorted(a, key = lambda x : (x[1], x[0])) )

list_of_triplets = [[1, 3, 6], [1, 3, 4], [1, 2, 7], [1, 1, 9], [1, 2, 3]]
list_of_triplets_copy = list_of_triplets

print(sorted(list_of_triplets))
print( sorted(list_of_triplets, key = lambda x: (x[0], x[1])) )
print( sorted(list_of_triplets, key = lambda x: (x[0], x[1], x[2])) )

list_of_triplets_copy.sort()
print(list_of_triplets_copy)

list_of_triplets_copy.sort(reverse=True)
print(list_of_triplets_copy)