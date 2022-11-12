#2231 분해합

import sys

N = int(sys.stdin.readline())

for num in range(1, N + 1):
    tmp = num

    #숫자가 한 자리수여도 전체 + 각 자리수를 해야 함
    for i in range(len(str(num))):
        tmp += int(str(num)[i])
    if tmp == N:
        print(num)
        break
else:
    print(0)