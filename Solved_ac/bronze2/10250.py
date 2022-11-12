#10250 ACM 호텔

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    floor = N % H
    if floor == 0:
        floor = H
    roomNum = (N - 1) // H + 1

    print(f'{floor}{roomNum:02}')