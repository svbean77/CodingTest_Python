#14652 나는 행복합니다~

N, M, K = map(int, input().split())

row = 0
col = K % M
while K > (M - 1):
    K -= M
    row += 1

print(row, col)