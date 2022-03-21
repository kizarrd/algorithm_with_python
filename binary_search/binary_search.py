def binary_search_loop(A, n):
    low, high = 0, len(A)-1
    while low <= high:
        mid = (low+high)//2

        if A[mid] == n: # 종료 조건1 검색 성공.
            return mid
        elif A[mid] > n:
            high = mid-1
        else:
            low = mid+1
    
    return -1 # 종료 조건2 (low > high) 검색 실패.
            
def binary_search_recursive(A, n, low, high):
    if low > high: # 종료 조건2 (low > high) 검색 실패.
        return -1
    
    mid = (low+high)//2

    if A[mid] == n: # 종료 조건1 검색 성공.
        return mid
    elif A[mid] > n:
        return binary_search_recursive(A, n, low, mid-1)
    else:
        return binary_search_recursive(A, n, mid+1, high)