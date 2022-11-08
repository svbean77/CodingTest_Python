#1085 직사각형에서 탈출

x, y, w, h = map(int, input().split())

root1 = abs(x - w)
root2 = abs(y - h)

print(min(x, y, root1, root2))