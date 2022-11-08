#2490 윷놀이

import sys

game = {1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        0: 'E'}

for _ in range(3):
    lst = list(map(int ,sys.stdin.readline().split()))

    print(game[lst.count(0)])