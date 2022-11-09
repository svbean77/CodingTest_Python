#2675 문자열 반복

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    R, S = sys.stdin.readline().split()
    S = list(S)

    for item in S:
        print(item * int(R), end = '')

    print()