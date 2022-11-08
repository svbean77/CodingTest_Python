#3009 네 번째 점

import sys

X = []
Y = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)

X.sort(); Y.sort()

tmp1 = X[1]
tmp2 = Y[1]
for _ in range(2):
    X.remove(tmp1)
    Y.remove(tmp2)

print(X[0], Y[0])