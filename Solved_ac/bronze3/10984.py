#10984 내 학점을 구해줘

import sys

T = int(sys.stdin.readline())


for _ in range(T):
    N = int(sys.stdin.readline())

    sub = 0
    avg = 0
    for __ in range(N):
        s, a = map(float, sys.stdin.readline().split())
        sub += int(s)
        avg += (a * int(s))

    print(f'{sub} {avg / sub:.1f}')