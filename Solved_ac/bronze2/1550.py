#1550 16진수

import sys

h = list(sys.stdin.readline().strip())
h = h[::-1]
num = 0
for i in range(len(h)):
    if h[i].isalpha():
        num += (ord(h[i]) - ord('A') + 10) * pow(16, i)
    else:
        num += int(h[i]) * pow(16, i)

print(num)