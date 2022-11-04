#2738 행렬 덧셈

N, M = map(int, input().split())

nLst = []
mLst = []

for _ in range(N):
    nLst.append(list(map(int, input().split())))

for _ in range(N):
    mLst.append(list(map(int, input().split())))

for n, m in zip(nLst, mLst):
    for i in range(M):
        print(n[i] + m[i], end = ' ')
    print()