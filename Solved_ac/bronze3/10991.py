#10991 별 찍기 - 16

import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    print(' ' * (N - i), end = '')
    print('* ' * i)
