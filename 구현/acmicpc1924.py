x, y = map(int, input().split())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayOfWeek = ('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')
print(dayOfWeek[(sum(days[:x])+y)%7])