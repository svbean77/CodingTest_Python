#9085 더하기

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(sum(lst))