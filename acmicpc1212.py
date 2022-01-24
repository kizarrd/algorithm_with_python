o = input()
binary = ''
for n in o:
    n = int(n)
    for i in range(2, -1, -1):
        if n >= 2**i:
            binary+='1'
            n-= 2**i
        else:
            binary+='0'

if binary[0] == '0' and len(binary) > 1:
    if binary[1] == '0':
        print(binary[2:])
    else:
        print(binary[1:])
else:
    print(binary)