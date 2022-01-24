import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

cnt = [0]
def merge(arr1, arr2):
    l, r = 0, 0
    merged = []
    l1, l2 = len(arr1), len(arr2)
    while l < l1 and r < l2:
        if arr1[l] > arr2[r]:
            merged.append(arr2[r])
            cnt[0] += len(arr1)-l
            r += 1
        else:
            merged.append(arr1[l])
            l += 1
    merged += arr1[l:]
    merged += arr2[r:]

    return merged

def mergeSort(start, end):
    if end - start == 1: return arr[start:end]
    mid = (start+end)//2
    return merge(mergeSort(start, mid), mergeSort(mid, end))

mergeSort(0, len(arr))
print(cnt[0]) 