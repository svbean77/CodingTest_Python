#10987 모음의 개수

import sys

word = list(sys.stdin.readline().strip())
Vowels = ['a', 'e', 'i', 'o', 'u']

cnt = 0
for item in word:
    if item in Vowels:
        cnt += 1

print(cnt)