from bisect import bisect_left, bisect_right

def lower_bound(A, n):
    low, high = 0, len(A)
    while low < high:
        mid = (low+high)//2
        if A[mid] >= n:
            high = mid
        else:
            low = mid+1

    return high
    # return low 해도 똑같다. low=high일때 종료되기 때문.

def upper_bound(A, n):
    low, high = 0, len(A)
    while low < high:
        mid = (low+high)//2
        if A[mid] > n:
            high = mid
        else:
            low = mid+1

    return high
    # return low 해도 똑같다. low=high일때 종료되기 때문.

a1 = [1, 2, 3, 3, 3, 4, 6, 7]

print(lower_bound(a1, 4), bisect_left(a1, 4))
print(upper_bound(a1, 4), bisect_right(a1, 4))

print(lower_bound(a1, 3), bisect_left(a1, 3))
print(upper_bound(a1, 3), bisect_right(a1, 3))

print(lower_bound(a1, 5), bisect_left(a1, 5))
print(upper_bound(a1, 5), bisect_right(a1, 5))

print(lower_bound(a1, 8), bisect_left(a1, 8))
print(upper_bound(a1, 8), bisect_right(a1, 8))

print(lower_bound(a1, 0), bisect_left(a1, 0))
print(upper_bound(a1, 0), bisect_right(a1, 0))