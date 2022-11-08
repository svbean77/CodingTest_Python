#1547 공

import sys

M = int(sys.stdin.readline())
ball = 1

for _ in range(M):
    X, Y = map(int ,sys.stdin.readline().split())

    if X == ball:
        ball = Y
    elif Y == ball:
        ball = X

print(ball)