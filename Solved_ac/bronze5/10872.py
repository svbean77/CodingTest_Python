#10872 팩토리얼

N = int(input())
fact = 1

for num in range(1, N + 1):
    fact *= num

print(fact)