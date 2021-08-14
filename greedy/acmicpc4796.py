#캠핑
cnt = 0
while True:
    l, p, v = map(int, input().split())
    if l==0 and p==0 and v==0:
        break
    day = 0
    cnt += 1

    rest = l if v%p>l else v%p
    day = (v//p)*l + rest

    print(f'Case {cnt}: {day}')