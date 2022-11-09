#1712 손익분기점

import sys

A, B, C = map(int, sys.stdin.readline().split())

computer = C - B

if computer > 0:
    print(A // computer + 1)
else:
    print(-1)