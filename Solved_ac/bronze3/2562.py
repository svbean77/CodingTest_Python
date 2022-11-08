#2562 최댓값

maximum = [0, 0]
for i in range(9):
    num = int(input())
    if num > maximum[1]:
        maximum[0] = i + 1
        maximum[1] = num

print(f'{maximum[1]}\n{maximum[0]}')
