#10992 별 찍기 - 17

import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    if i == N:
        print('*' * (2 * N - 1))
    elif i == 1:
        print(' ' * (N - i), end = '')
        print('*')
    else:
        print(' ' * (N - i), end = '')
        print('*', end = '')
        print(' ' * (2 * (i - 1) - 1), end = '')
        print('*')