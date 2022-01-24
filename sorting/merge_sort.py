a = [9, 1, 3, 2, 4, 8, 7, 5, 6]

def merge(arr1, arr2):
    l, r = 0, 0
    merged = []
    l1, l2 = len(arr1), len(arr2)
    while l < l1 and r < l2:
        if arr1[l] > arr2[r]:
            merged.append(arr2[r])
            r += 1
        else:
            merged.append(arr1[l])
            l += 1
    merged += arr1[l:] # 이렇게 하는 대신 extend함수를 사용하는 것도 봤음. 
    merged += arr2[r:]

    return merged

def mergeSort(start, end):
    if end - start == 1: return a[start:end]
    mid = (start+end)//2
    return merge(mergeSort(start, mid), mergeSort(mid, end))

print(mergeSort(0, len(a)))