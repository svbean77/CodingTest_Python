#3003 킹, 퀸, 룩, 비숍, 나이트, 폰

findPiece = list(map(int, input().split()))
correctPiece = [1, 1, 2, 2, 2, 8]

for i in range(len(findPiece)):
    print(correctPiece[i] - findPiece[i], end = ' ')