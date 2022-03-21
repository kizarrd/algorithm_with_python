S = input()
alpha_counter = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for a in alphabet:
    alpha_counter[a] = 0
for a2 in S:
    alpha_counter[a2] += 1
for a3 in alphabet:
    print(alpha_counter[a3], end=' ')