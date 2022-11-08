#10886 0 = not cute/ 1 = cute

import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]

if lst.count(0) > lst.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')