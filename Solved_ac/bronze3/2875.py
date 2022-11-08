#2875 대회 or 인턴

import sys

N, M, K = map(int, sys.stdin.readline().split())

while K != 0:
    if (N % 2 != 0):
        N -= 1
        K -= 1
    elif (2 * M > N):
        M -= 1
        K -= 1
    else:
        N -= 1
        K -= 1

cnt = 0
while (M != 0 and N >= 2):
    N -= 2
    M -= 1
    cnt += 1

print(cnt)