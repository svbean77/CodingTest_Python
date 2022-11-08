#10833 사과

import sys

N = int(sys.stdin.readline())

tmp = 0
for _ in range(N):
    student, apple = map(int, sys.stdin.readline().split())

    tmp += (apple % student)

print(tmp)