a, b = input().split()
b = int(b)
_int, _real = a.split('.')

if _int == '0':
    powered = str(int(_real)**b)
    print('0.'+'0'*(len(_real)*b-len(powered))+powered)
else:
    powered = str(int(_int+_real)**b)
    dot_location = len(powered)-len(_real)*b
    print(powered[:dot_location]+'.'+powered[dot_location:])