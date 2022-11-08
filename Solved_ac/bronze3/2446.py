#2446 별 찍기 - 9

import sys

N = int(sys.stdin.readline())

for i in range(N, 0, -1):
    print(' ' * (N - i), end = '')
    print('*' * (2 * i - 1))

for i in range(2, N + 1):
    print(' ' * (N - i), end = '')
    print('*' * (2 * i - 1))