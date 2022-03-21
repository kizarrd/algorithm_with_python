N = int(input())

def hanoi(n, a, b, c): # 이 함수의 기능은 n개의 원판을 a로부터 c로 이동시키는 것이다.
    if n == 1: # 만약 이동하고자 하는 원판이 한개라면 실제 이동을 수행하고, 더이상의 이동을 막기 위해 함수를 종료한다.
        moves.append((a, c))
        return

    hanoi(n-1, a, c, b) # 가장 아래의 원판을 제외하고 나머지 원판들을 이동하고자 하는 칸 말고 다른 칸으로 옮기기
    hanoi(1, a, b, c) # 가장 아래의 원판을 이동하고자 하는 칸으로 옮기기
    hanoi(n-1, b, a, c) # 가장 아래의 원판을 제외하고 나머지 원판들을 다시 이동하고자 하는 칸으로 옮기기

moves = []
hanoi(N, 1, 2, 3) # "N개의 원판을 a로부터 c로 이동시켜라"
print(len(moves))
for _from, _to in moves:
    print(_from, _to)