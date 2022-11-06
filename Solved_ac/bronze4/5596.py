#5596 시험 점수

Min = list(map(int, input().split()))
Man = list(map(int, input().split()))

if sum(Min) < sum(Man):
    print(sum(Man))
else:
    print(sum(Min))