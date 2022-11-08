#10214 Baseball

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    Y = 0
    K = 0
    for __ in range(9):
        y, k = map(int, sys.stdin.readline().split())
        Y += y
        K += k

    if Y > K:
        print('Yonsei')
    elif Y < K:
        print('Korea')
    else:
        print('Draw')