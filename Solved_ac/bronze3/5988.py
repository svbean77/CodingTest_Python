#5988 홀수일까 짝수일까

import sys

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    if num % 2 == 0:
        print('even')
    else:
        print('odd')