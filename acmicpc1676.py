N = int(input())

five_count = 0
five_powers = 5
multiplier = 1
while True:
    five_multiplied = five_powers*multiplier
    if five_multiplied > N:
        if five_powers*5 > N:
            break
        else:
            five_powers*=5
            multiplier = 1
    else:
        five_count += 1
        multiplier += 1

print(five_count)