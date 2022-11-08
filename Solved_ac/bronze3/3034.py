#3034 앵그리 창영

import sys
from math import sqrt

N, W, H = map(int, sys.stdin.readline().split())

for _ in range(N):
    length = int(sys.stdin.readline())

    #성냥을 대각선으로 넣는 경우도 고려
    diag = sqrt(pow(W, 2) + pow(H, 2))
    if (length <= W) or (length <= H) or (length <= diag):
        print('DA')
    else:
        print('NE')