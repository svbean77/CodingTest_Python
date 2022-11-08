#2576 홀수

import sys

sum = 0
minimum = 100

for _ in range(7):
    num = int(sys.stdin.readline())

    if num % 2 != 0:
        sum += num
        if num < minimum:
            minimum = num


if sum != 0:
    print(f'{sum}\n{minimum}')
else:
    print(-1)