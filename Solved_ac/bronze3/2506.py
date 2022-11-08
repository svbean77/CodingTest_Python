#2506 점수계산

import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

score = 0
add = 1

for i in range(N):
    if lst[i] == 1:
        if i != 0:
            if lst[i - 1] == 1:
                add += 1
        score += add
    else:
        add = 1

print(score)