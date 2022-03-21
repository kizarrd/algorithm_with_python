N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N
for n_applicants in A:
    n_applicants -= B
    if n_applicants > 0:
        cnt += n_applicants//C
        if n_applicants%C > 0:
            cnt += 1

print(cnt)