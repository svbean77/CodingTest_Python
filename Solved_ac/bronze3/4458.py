#4458 첫 글자를 대문자로

import sys

N = int(sys.stdin.readline())

for _ in range(N):
    sentence = sys.stdin.readline().strip()

    for i in range(len(sentence)):
        if i == 0:
            print(sentence[i].upper(), end = '')
        else:
            print(sentence[i], end = '')
    print()