#10162 전자레인지

import sys

T = int(sys.stdin.readline())

A = T // 300
T %= 300
B = T // 60
T %= 60
C = T // 10

if (T % 10) != 0:
    print(-1)
else:
    print(A, B, C)