#2920 음계

import sys

num = list(map(int, sys.stdin.readline().split()))

if num == sorted(num):
    result = 'ascending'
elif num == sorted(num)[::-1]:
    result = 'descending'
else:
    result = 'mixed'

print(result)