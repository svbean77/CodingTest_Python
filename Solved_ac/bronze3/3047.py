#3047 ABC

import sys

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
mapping = {'A': lst[0], 'B': lst[1], 'C': lst[2]}

word = list(sys.stdin.readline().strip())

print(mapping[word[0]], mapping[word[1]], mapping[word[2]])