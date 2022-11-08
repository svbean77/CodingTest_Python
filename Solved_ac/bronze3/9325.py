#9325 얼마?

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    s = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for __ in range(n):
        q, p = map(int ,sys.stdin.readline().split())

        s += (q * p)

    print(s)