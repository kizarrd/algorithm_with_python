N = int(input())

neg_binary = ''
while N != 0:
    if N%(-2):
        neg_binary += '1'
        N = N//(-2) + 1
    else:
        neg_binary += '0'
        N//=(-2)

if neg_binary:
    print(neg_binary[::-1])
else:
    print(0)
