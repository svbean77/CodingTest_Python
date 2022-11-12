#1100 하얀 칸

import sys

cnt = 0

for i in range(8):
    chess = sys.stdin.readline().rstrip()

    for j in range(8):
        if i % 2 == 0:
            if (j % 2 == 0) and (chess[j] == 'F'):
                cnt += 1
        else:
            if (j % 2 != 0) and (chess[j] == 'F'):
                cnt += 1

print(cnt)