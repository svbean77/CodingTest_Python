#2965 캥거루 세마리

import sys

A, B, C = map(int, sys.stdin.readline().split())

#가장 바깥쪽의 캥거루가 한 칸씩 이동하는 것이 최대이기 때문에 B-A or C-B
#같은 좌표에 위치할 수 없기 때문에 -1
case1 = (B - A) - 1
case2 = (C - B) - 1

print(max(case1, case2))