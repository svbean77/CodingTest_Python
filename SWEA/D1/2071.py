#2071 평균값 구하기

T = int(input())
for idx in range(1, T + 1):
    num = list(map(int, input().split()))
    m = int(round(sum(num) / 10, 0))
    print("#{0} {1}".format(idx, m))