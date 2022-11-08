#5086 배수와 약수

import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        if(A == 0) & (B == 0):
            break
        if B % A == 0:
            print('factor')
        elif A % B == 0:
            print('multiple')
        else:
            print('neither')

    except EOFError:
        break