#1009 분산처리

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    # 0~9의 n제곱을 했을 때 길어도 네 번만 반복됨 -> 어차피 일의 자리만 구하면 되기 때문에 각각 나눠서 사용
    # 0
    # 1
    # 2 4 8 6
    # 3 9 7 1
    # 4 6
    # 5
    # 6
    # 7 9 3 1
    # 8 4 2 6
    # 9 1
    a %= 10
    b %= 4
    if b == 0:
        b = 4
    data = pow(a, b)
    if data % 10 == 0:
        print(10)
    else:
        print(data % 10)

