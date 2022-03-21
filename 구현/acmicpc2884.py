H, M = map(int, input().split())

if M < 45:
    M = M+60-45
    H = (H+24-1)%24
else:
    M = M-45
print(H, M)