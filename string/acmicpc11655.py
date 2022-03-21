S = input()
n_alphabet = ord('Z')-ord('A')+1
for s in S:
    char = s
    if s.isupper():
        char = chr(((ord(s)+13-ord('A'))%n_alphabet)+ord('A'))
    elif s.islower():
        char = chr(((ord(s)+13-ord('a'))%n_alphabet)+ord('a'))
    print(char, end='')