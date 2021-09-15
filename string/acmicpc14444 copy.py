#LEET 5 대신 풀어보는 것.
S = input()

def expand(left: int, right: int) -> int:
    while left >= 0 and right <len(S) and S[left] == S[right]:
        left -= 1
        right +=1
    return len(S[left+1:right])

if len(S)<2 or S == S[::-1]:
    print(len(S))
else:
    result = 0
    for i in range(len(S)-1):
        result = max(result, expand(i, i+1), expand(i, i+2))
    print(result)