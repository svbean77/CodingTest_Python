#2444 별 찍기 -7

import sys
N = int(sys.stdin.readline())

for i in range(1, N + 1):
    print(' ' * (N - i), end = '')
    print('*' * (2 * i - 1))

for i in range(N - 1, 0, -1):
    print(' ' * (N - i), end = '')
    print('*' * (2 * i - 1))