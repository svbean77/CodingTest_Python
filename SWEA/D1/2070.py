#2070 큰 놈, 작은 놈, 같은 놈

T = int(input())

for idx in range(1, T + 1):
    a, b = map(int, input().split())

    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    else:
        result = '='

    print('#{0} {1}'.format(idx, result))