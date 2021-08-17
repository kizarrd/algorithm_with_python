#체스판 다시 칠하기
n, m = map(int, input().split())
board = [ input().rstrip() for _ in range(n)]
min=64
for i in range(n-7):
    for j in range(m-7):
        count=0
        # first coordinate B
        i2 = i
        j2 = j
        for k in range(8):
            for l in range(8):
                if k%2==0:
                    if l%2==0:
                        if board[i2][j2]!='B':
                            count+=1
                    else:
                        if board[i2][j2]!='W':
                            count+=1
                else:
                    if l%2==0:
                        if board[i2][j2]!='W':
                            count+=1
                    else:
                        if board[i2][j2]!='B':
                            count+=1    
                j2+=1
            j2=j
            i2+=1
        min = count if count<min else min
        count = 0
        # first coordinate W
        i2 = i
        j2 = j
        for k in range(8):
            for l in range(8):
                if k%2==0:
                    if l%2==0:
                        if board[i2][j2]!='W':
                            count+=1
                    else:
                        if board[i2][j2]!='B':
                            count+=1
                else:
                    if l%2==0:
                        if board[i2][j2]!='B':
                            count+=1
                    else:
                        if board[i2][j2]!='W':
                            count+=1    
                j2+=1
            j2=j
            i2+=1
        min = count if count<min else min
        count = 0

print(min)