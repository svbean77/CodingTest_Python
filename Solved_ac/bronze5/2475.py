#2475 검증수

lst = list(map(int, input().split()))
sum = 0

for num in lst:
    sum += pow(num, 2)

print(sum % 10)