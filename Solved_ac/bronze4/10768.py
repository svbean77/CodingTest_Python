#10768 특별한 날

M = int(input())
D = int(input())

if (M == 2) & (D == 18):
    day = 'Special'
elif (M < 2) | ((M == 2) & (D < 18)):
    day = 'Before'
else:
    day = 'After'

print(day)
