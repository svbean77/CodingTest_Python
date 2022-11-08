#3058 짝수를 찾아라

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    lst = list(map(int, sys.stdin.readline().split()))
    sum = 0
    minimum = 100

    for num in lst:
        if num % 2 == 0:
            sum += num
            if num < minimum:
                minimum = num

    print(sum, minimum)