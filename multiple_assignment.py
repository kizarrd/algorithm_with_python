x = 1
y = 2

print('x = 1')
print('y = 2')
while True:
    cmd = input('want multiple assignment? (y/n)\n')
    if cmd == 'y':
        x, y = y, x
        print('x, y = y, x')
        print(f'then, x = {x} and y = {y}')
        break
    elif cmd == 'n':
        x = y
        y = x
        print('x = y')
        print('y = x')
        print(f'then, x = {x} and y = {y}')
        break
    else:
        print('input is wrong, do it again')