#10103 주사위 게임

import sys

n = int(sys.stdin.readline())

score = [100, 100]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if (a > b):
        score[1] -= a
    elif (a < b):
        score[0] -= b

print(f'{score[0]}\n{score[1]}')