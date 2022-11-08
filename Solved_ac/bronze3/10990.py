#10990 별 찍기 - 15

import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    if i == 1:
        print(' ' * (N - i), end = '')
        print('*')
    else:
        print(' ' * (N - i), end = '')
        print('*', end = '')
        print(' ' * (2 * i - 3), end = '')
        print('*')