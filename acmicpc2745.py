N, B = input().split()
answer = 0
for i in range(1, len(N)+1):
    val = None
    if N[-i].isalpha():
        val = ord(N[-i])-ord('A')+10
    else:
        val = int(N[-i])
    answer += val*(int(B)**(i-1))

print(answer)