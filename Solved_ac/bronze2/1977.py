#1977 완전제곱수

import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

s = 0
m = N

for num in range(M, N + 1):
    #1도 완전제곱수이지만 for문 범위에 포함되지 않기 때문에 2를 더해줌
    for i in range(1, num // 2 + 2):
        if i * i == num:
            s += num
            if num < m:
                m = num

if s == 0:
    print(-1)
else:
    print(f'{s}\n{m}')