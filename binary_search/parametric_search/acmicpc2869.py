A, B ,V = map(int, input().split())

start, end = 0, V//(A-B) if (A-B)*(V//(A-B)) == V else V//(A-B)+1
ansewr = 0

while start <= end:
    mid = (start+end)//2

    reachable = (A-B)*(mid-1)+A

    if reachable >= V:
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)