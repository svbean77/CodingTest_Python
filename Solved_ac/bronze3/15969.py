#15969 행복

import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

print(max(lst) - min(lst))