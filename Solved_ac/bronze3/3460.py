#3460 이진수

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    num = str(bin(int(sys.stdin.readline())))
    num = num[2:]

    for i in range(len(num) - 1, -1, -1):
        if num[i] == '1':
            print(len(num) - i - 1, end = ' ')
    print()