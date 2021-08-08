N = int(input())

counter = 0;
for i in range(1, N+1):
    if i < 100 :
        counter+=1
        continue
    n = str(i)
    hanNumber = True;
    for i in range(len(n)-2):
        if int(n[i])-int(n[i+1]) != int(n[i+1])-int(n[i+2]):
            hanNumber = False;
            break;
    if hanNumber:
        counter+=1

print(counter)