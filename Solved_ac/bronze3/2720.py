#2720 세탁소 사장 동혁

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    C = int(sys.stdin.readline())

    Q = C // 25
    C %= 25
    D = C // 10
    C %= 10
    N = C // 5
    C %= 5

    print(Q, D, N, C)