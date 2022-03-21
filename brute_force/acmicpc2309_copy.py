# 9난쟁중 7난쟁을 고르는 것은 9난쟁중 2난쟁을 고르는 경우의 수와 같다.
# 그리고 실제로 2난쟁을 고르는 것을 구현하여 풀 수 있다.
height_of_dwarf = []
for _ in range(9):
    height_of_dwarf.append(int(input()))
height_of_dwarf.sort()
total = sum(height_of_dwarf)
for i in range(9):
    for j in range(i+1, 9):
        if total - height_of_dwarf[i] - height_of_dwarf[j] == 100:
            for k in range(9):
                if k!=i and k!=j:
                    print(height_of_dwarf[k])
            exit()