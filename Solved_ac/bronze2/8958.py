#8958 OX퀴즈

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    sum = 0
    add = 1
    case = list(sys.stdin.readline().strip())

    for i in range(len(case)):
        if case[i] == 'O':
            if i == 0:
                sum += add
            else:
                if case[i - 1] == 'O':
                    add += 1
                sum += add
        else:
            add = 1

    print(sum)