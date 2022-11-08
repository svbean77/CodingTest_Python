#9610 사분면

import sys

n = int(sys.stdin.readline())

cnt = [0, 0, 0, 0, 0]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if (x > 0) and (y > 0):
        cnt[0] += 1
    elif (x < 0) and (y > 0):
        cnt[1] += 1
    elif (x < 0) and (y < 0):
        cnt[2] += 1
    elif (x > 0) and (y < 0):
        cnt[3] += 1
    else:
        cnt[4] += 1

for i in range(4):
    print(f'Q{i+1}: {cnt[i]}')
print(f'AXIS: {cnt[-1]}')