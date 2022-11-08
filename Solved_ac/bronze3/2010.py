#2010 플러그

import sys

N = int(sys.stdin.readline())

sum = 1

for _ in range(N):
    num = int(sys.stdin.readline()) - 1
    sum += num

print(sum)