#2056 연월일 달력

T = int(input())

days = [[1, 31], [1, 28], [1, 31], [1, 30], [1, 31], [1, 30], [1, 31], [1, 31], [1, 30], [1, 31], [1, 30], [1, 31]]
for idx in range(1, T + 1):
    date = input()
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])

    if (month < 1) or (month > 12):
        print('#{} {}'.format(idx, -1))
    elif (day < days[month - 1][0]) or (day > days[month - 1][1]):
        print('#{} {}'.format(idx, -1))
    else:
        print('#{} {:04}/{:02}/{:02}'.format(idx, year, month, day))