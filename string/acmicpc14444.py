#LEET 5 대신 풀어보는 것.
S = input()

if len(S)<2 or S == S[::-1]:
    print(len(S))
else:
    longest_length = 0
    for i in range(len(S)-1):
        for j in range(len(S), i, -1):
            if len(S[i:j]) > longest_length and S[i:j] == S[i:j][::-1]:
                longest_length = len(S[i:j])
    print(longest_length)

#시간 초과