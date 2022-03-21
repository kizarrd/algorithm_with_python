target_value = None
low, high = None, None # 신중히 잘 정해야 함.
answer = 0
while low <= high:
    mid = (low+high)//2

    # do the decision process
    decision_value = None

    # this part can be different, depending on the context. e.g. a_value <= target_values:
    if decision_value >= target_value: 
        answer = mid
        high = mid-1 # can be different e.g. low = mid+1
    else:
        low = mid+1 # can be different e.g. high = mid-1

print(answer)