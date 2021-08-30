q = [1, 2, 3]
q2 = [1]

while q:
    if q.pop(0) != q.pop():
        print("not equal")
    else:
        print("equal")
