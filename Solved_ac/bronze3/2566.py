#2566 최댓값

import sys

row = 0
col = 0
maximum = -1
for i in range(1, 10):
    lst = list(map(int, sys.stdin.readline().split()))

    tmp = max(lst)
    if tmp > maximum:
        row = i
        col = lst.index(tmp) + 1
        maximum = tmp

print(maximum)
print(row, col)