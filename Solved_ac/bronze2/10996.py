#10996 별 찍기 - 21

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    print('* ' * ((n + 1) // 2))
    if n != 1:
        print(' *' * (n // 2))