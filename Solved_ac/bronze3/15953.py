#15953 상금 헌터

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    reward = 0

    if (a >= 1) and (a <= 21):
        if a == 1:
            reward += 500
        elif a <= 3:
            reward += 300
        elif a <= 6:
            reward += 200
        elif a <= 10:
            reward += 50
        elif a <= 15:
            reward += 30
        else:
            reward += 10
    if (b >= 1) and (b <= 31):
        if b == 1:
            reward += 512
        elif b <= 3:
            reward += 256
        elif b <= 7:
            reward += 128
        elif b <= 15:
            reward += 64
        else:
            reward += 32

    print(reward * 10000)