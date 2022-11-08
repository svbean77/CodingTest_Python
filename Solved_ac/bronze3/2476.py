#2476 주사위 게임

import sys

N = int(sys.stdin.readline())
award = 0

for _ in range(N):
    x, y, z = map(int, sys.stdin.readline().split())

    if len({x, y, z}) == 1:
        tmp = 10000 + x * 1000
    elif (x == y) or (x == z):
        tmp = 1000 + x * 100
    elif (y == z):
        tmp = 1000 + y * 100
    else:
        tmp = max(x, y, z) * 100

    if award < tmp:
        award = tmp

print(award)